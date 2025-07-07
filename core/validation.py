from enum import Enum
from typing import List, Dict, Any, Optional, NamedTuple
from core.agent import AgentToolCall
# from agent import AgentToolCall

class ErrorType(Enum):
    MISSING_FUNCTION = "missing_function"  # Expected function call is missing
    MISSING_ARGUMENT = "missing_argument"  # Expected argument is missing
    WRONG_ARGUMENT_TYPE = "wrong_argument_type"  # Wrong type of argument
    WRONG_ARGUMENT_VALUE = "wrong_argument_value"  # Wrong value of argument

# Define a validation error structure
class ValidationError(NamedTuple):
    error_type: ErrorType
    message: str
    call_index: Optional[int] = None
    arg_name: Optional[str] = None

# Update the validation function to return structured errors
def validate_function_calls(actual_calls: List[AgentToolCall],
                          expected_calls: List[Dict[str, Any]]) -> List[ValidationError]:
    """
    Validate that actual function calls match expected calls.
    
    Args:
        actual_calls: List of actual function calls from the tracker
        expected_calls: List of expected function calls from ground_truths.json
        
    Returns:
        List of validation errors with structured type information
    """
    errors = []
    
    # Create a copy of actual_calls to mark matches
    remaining_actual_calls = list(actual_calls)
    
    # For each expected call, try to find a matching actual call
    for i, expected in enumerate(expected_calls):
        expected_name = expected["name"]
        is_required = expected.get("required", True)  # Default to True if not specified
        
        # Find a matching function call by name
        match_found = False
        match_index = None
        
        for j, actual in enumerate(remaining_actual_calls):
            if actual.function == expected_name:
                match_found = True
                match_index = j
                break
        
        if not match_found:
            # Only report missing functions that are required
            if is_required:
                errors.append(ValidationError(
                    error_type=ErrorType.MISSING_FUNCTION,
                    message=f"Missing required function call: {expected_name}",
                    call_index=i
                ))
            continue
        
        # Validate arguments of the matching call
        actual_call = remaining_actual_calls[match_index]
        argument_errors = validate_arguments(actual_call, expected, i)
        errors.extend(argument_errors)
        
        # Remove the matched call so we don't match it again
        remaining_actual_calls.pop(match_index)
    
    return errors

def validate_arguments(actual: AgentToolCall,
                     expected: Dict[str, Any],
                     call_index: int) -> List[ValidationError]:
    """
    Validate arguments of a function call with smarter handling of renamed parameters.
    
    Args:
        actual: Actual function call record
        expected: Expected function call
        call_index: Index of this call
    """
    actual_args = actual.arguments
    expected_args = expected.get("arguments", [])
    errors = []
    
    # Keep track of matched arguments on both sides
    matched_actual_args = set()
    matched_expected_args = set()
    
    # First check all expected arguments
    for arg_index, expected_arg in enumerate(expected_args):
        if "name" not in expected_arg:
            errors.append(ValidationError(
                error_type=ErrorType.MISSING_ARGUMENT,
                message=f"Call {call_index+1}, Arg {arg_index+1}: Expected argument is missing required 'name' field",
                call_index=call_index
            ))
            continue
        
        expected_name = expected_arg["name"]

        is_required = expected_arg.get("required", True)  # Default to True if not specified
        if is_required and expected_name not in actual_args:
            errors.append(ValidationError(
                error_type=ErrorType.MISSING_ARGUMENT,
                message=f"Call {call_index+1}: Expected parameter '{expected_name}' not found in actual arguments",
                call_index=call_index,
                arg_name=expected_name
            ))
            continue
        
        if expected_name in actual_args:
            # Found a matching named parameter
            actual_value = actual_args[expected_name]
            matched_actual_args.add(expected_name)
            matched_expected_args.add(expected_name)
            
            # Validate value if specified
            if "value" in expected_arg:
                expected_value = expected_arg["value"]
                # if actual_value in expected_value:
                if is_valid(actual_value, expected_value):
                    pass
                else:
                    print(str(actual_value), str(expected_value))
                    errors.append(ValidationError(
                        error_type=ErrorType.WRONG_ARGUMENT_VALUE,
                        message=f"Call {call_index+1}, Arg '{expected_name}': Expected value '{expected_value}', got '{actual_value}'",
                        call_index=call_index,
                        arg_name=expected_name
                    ))
            
            # Validate type if specified
            if "type" in expected_arg:
                expected_type = expected_arg["type"]
                actual_type = type(actual_value).__name__
                if actual_type == "NoneType":
                    continue
                if actual_type == expected_type:
                    pass
                elif  actual_type == "str" and expected_type == "string":
                    pass
                elif actual_type == "int" and expected_type == "integer":
                    pass  
                elif actual_type == "bool" and expected_type == "boolean":
                    pass  
                else:
                    errors.append(ValidationError(
                        error_type=ErrorType.WRONG_ARGUMENT_TYPE,
                        message=f"Call {call_index+1}, Arg '{expected_name}': Expected type '{expected_type}', got '{actual_type}'",
                        call_index=call_index,
                        arg_name=expected_name
                    ))
    
    return errors

def strict_equality_matcher(spec_value, allowed_values: list) -> bool:
    if spec_value is None:
        return '' in allowed_values

    if not isinstance(allowed_values, list):
        return (spec_value)==str(allowed_values)
    return spec_value in allowed_values

def is_valid(spec, options, key_map: dict = None, matcher=strict_equality_matcher) -> bool:
    # 分支 1: spec 是一个字典
    if isinstance(spec, dict):
        return _validate_dict(spec, options, key_map, matcher)

    # 分支 2: spec 是一个列表
    if isinstance(spec, list):
        return _validate_list(spec, options)
    
    # 分支 3: spec 是一个单一值 (这是递归的最终出口)
    return matcher(spec, options)

def _validate_dict(spec_dict: dict, options_obj, key_map: dict, matcher) -> bool:
    """
    (辅助函数) 专门处理字典类型的 spec 验证。
    """
    if not isinstance(options_obj, dict):
        # print(f"验证失败: 需求是一个字典, 但对应的选项不是 (而是 {type(options_obj).__name__})。")
        return False

    for spec_key, spec_value in spec_dict.items():
        mapped_keys = key_map.get(spec_key, spec_key)
        if not isinstance(mapped_keys, list):
            mapped_keys = [mapped_keys]

        key_is_validated = False
        for options_key in mapped_keys:
            if options_key not in options_obj:
                continue
            
            options_for_key = options_obj.get(options_key)
            
            # 关键的递归调用：返回到主函数 is_valid，以处理 spec_value 可能的任何类型
            if is_valid(spec_value, options_for_key, key_map, matcher):
                key_is_validated = True
                break
        
        if not key_is_validated:
            # print(f"验证失败: 字典中的键 '{spec_key}' (值: '{spec_value}') 未通过验证。")
            return False
            
    return True


def _validate_list(spec_list: list, options_obj) -> bool:
    """
    (辅助函数) 专门处理列表类型的 spec 验证 (执行子集检查)。
    """
    if not isinstance(options_obj, list):
        # print(f"验证失败: 需求是一个列表, 但对应的选项不是 (而是 {type(options_obj).__name__})。")
        return False

    # 检查 spec_list 中的每个元素是否存在于 options_obj 中
    # 注意：此简单实现主要用于处理原始类型（字符串、数字）的列表。
    for item in spec_list:
        if item not in options_obj:
            # print(f"验证失败: 列表中的元素 '{item}' 不在允许的选项列表中。")
            return False
            
    return True

if __name__ == "__main__":
    # actual_calls = [
    #     AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797", "seat_class": "premium_economy"},call_id=0),
    #     AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797"},call_id=1),
    # ]
    # expected_calls = [{"name": "check_seat_availability", "arguments": [{"name": "flight_id", "value": "LH797", "type": "str"}, {"name": "seat_class", "value": "premium_economy", "type": "str"}]}]
    # print(validate_function_calls(actual_calls, expected_calls))

    actual = AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797", "seat_class": "premium_economy"},call_id=0)
    expected = {'name': 'check_seat_availability', 'arguments': [{'name': 'flight_id', 'value': ['LH797','lh97'], 'type': 'str'}, {'name': 'seat_class', 'value': ['premium_economy'], 'type': 'str'}]}
    argument_errors = validate_arguments(actual, expected, 0)