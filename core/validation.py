from enum import Enum
from typing import List, Dict, Any, Optional, NamedTuple
from core.agent import AgentToolCall

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

def validate_function_calls(actual_calls: List[AgentToolCall],
                          expected_calls: List[Dict[str, Any]]) -> List[ValidationError]:
    """Simple validation handling mismatched counts"""
    from collections import defaultdict
    
    errors = []
    
    # Group actual calls by function name
    actual_groups = defaultdict(list)
    for call in actual_calls:
        actual_groups[call.function].append(call)
    
    expected_groups = defaultdict(list)
    for i, expected in enumerate(expected_calls):
        expected_groups[expected["name"]].append((i, expected))
    
    # Validate each expected function
    for func_name, expected_list in expected_groups.items():
        actual_list = actual_groups.get(func_name, [])
        
        # Simple strategy: as long as actual count >= expected count
        required_count = sum(1 for _, exp in expected_list if exp.get("required", True))
        
        if len(actual_list) < required_count:
            errors.append(ValidationError(
                error_type=ErrorType.MISSING_FUNCTION,
                message=f"Function '{func_name}' called {len(actual_list)} times, expected at least {required_count}",
            ))
            continue
        
        # Try to match: find the most similar actual for each expected
        used_actual_indices = set()
        
        for exp_index, expected in expected_list:
            best_match_idx = None
            best_score = float('inf')
            
            # Find the best matching actual call
            for j, actual in enumerate(actual_list):
                if j in used_actual_indices:
                    continue
                    
                score = calculate_mismatch_cost(actual, expected)
                if score < best_score:
                    best_score = score
                    best_match_idx = j
            
            if best_match_idx is not None:
                # Validate parameters
                used_actual_indices.add(best_match_idx)
                argument_errors = validate_arguments(actual_list[best_match_idx], expected, exp_index, func_name)
                errors.extend(argument_errors)
            elif expected.get("required", True):
                errors.append(ValidationError(
                    error_type=ErrorType.MISSING_FUNCTION,
                    message=f"No suitable match found for required function call: {func_name}",
                    call_index=exp_index
                ))
    
    return errors

def calculate_mismatch_cost(actual: AgentToolCall, expected: Dict[str, Any]) -> float:
    """Calculate the mismatch cost between actual and expected arguments"""
    expected_args = expected.get("arguments", [])
    if not expected_args:
        return 0.0
    
    total_cost = 0.0
    total_weight = 0.0
    
    for expected_arg in expected_args:
        if "name" not in expected_arg:
            continue
            
        expected_name = expected_arg["name"]
        weight = 1.0
        
        if expected_name not in actual.arguments:
            if expected_arg.get("required", True):
                total_cost += 1.0  # Fixed cost for missing required parameters
            total_weight += weight
            continue
        
        actual_value = actual.arguments[expected_name]
        
        # Value matching check
        if "value" in expected_arg:
            if normalize_value(actual_value) != normalize_value(expected_arg["value"]):
                total_cost += 0.5  # Value mismatch cost    
            total_weight += 1.0
        
        # Type matching check  
        if "type" in expected_arg:
            if not is_type_compatible(actual_value, expected_arg["type"]):
                total_cost += 0.3  # Type mismatch cost
            total_weight += 0.5
    
    return total_cost / max(total_weight, 1.0)

def normalize_value(value):
    """Normalize value for comparison, handle type conversion"""
    if isinstance(value, (int, float)):
        # Normalize numeric values
        if isinstance(value, float) and value == int(value):
            return str(int(value))  # 6.0 -> '6'
        elif isinstance(value, float):
            return f"{value:g}"     # Remove trailing zeros: 5.60 -> '5.6'
        else:
            return str(value)       # int -> str
    
    return str(value).strip()

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
                if str(actual_value) != str(expected_value):
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
                if actual_type != expected_type:
                    errors.append(ValidationError(
                        error_type=ErrorType.WRONG_ARGUMENT_TYPE,
                        message=f"Call {call_index+1}, Arg '{expected_name}': Expected type '{expected_type}', got '{actual_type}'",
                        call_index=call_index,
                        arg_name=expected_name
                    ))
    
    return errors

if __name__ == "__main__":
    actual_calls = [
        AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797", "seat_class": "premium_economy"}),
        AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797"}),
    ]
    expected_calls = [{"name": "check_seat_availability", "arguments": [{"name": "flight_id", "value": "LH797", "type": "str"}, {"name": "seat_class", "value": "premium_economy", "type": "str"}]}]
    print(validate_function_calls(actual_calls, expected_calls))
