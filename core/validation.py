from enum import Enum
from typing import List, Dict, Any, Optional, NamedTuple
from core.agent import AgentToolCall
# from agent import AgentToolCall
from core.complex_value_validation import validate_argument as complex_validate_argument
import typing

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
        if isinstance(actual_call,str) and "^" in actual_call:
            actual_call = actual_call.replace("^", "**")

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
        if is_required is False:
            continue
        
        if expected_name in actual_args:
            # Found a matching named parameter
            actual_value = actual_args[expected_name]
            matched_actual_args.add(expected_name)
            matched_expected_args.add(expected_name)

            if "value" in expected_arg and "type" in expected_arg:
                expected_value = expected_arg["value"]
                expected_type = expected_arg["type"]
                status,error = complex_validate_argument(actual_value, expected_arg, call_index)
                if status == False:
                    errors.append(error)
    
    return errors



if __name__ == "__main__":
    # actual_calls = [
    #     AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797", "seat_class": "premium_economy"},call_id=0),
    #     AgentToolCall(function="check_seat_availability", arguments={"flight_id": "LH797"},call_id=1),
    # ]
    # expected_calls = [{"name": "check_seat_availability", "arguments": [{"name": "flight_id", "value": "LH797", "type": "str"}, {"name": "seat_class", "value": "premium_economy", "type": "str"}]}]
    # print(validate_function_calls(actual_calls, expected_calls))

    actual = AgentToolCall(function="calculate_fitness", arguments={"trait_values": [0.8,0.7], "trait_contributions": [0.4, 0.6]}, call_id=0)
    expected = {'name': 'calculate_fitness', 'arguments': [{'name': 'trait_values', 'value': [[0.8, 0.7]], 'type': List[float]}, {'name': 'trait_contributions', 'value': [[0.4, 0.6]], 'type': List[float]}]}
    argument_errors = validate_arguments(actual, expected, 0)
    print(argument_errors)