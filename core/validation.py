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