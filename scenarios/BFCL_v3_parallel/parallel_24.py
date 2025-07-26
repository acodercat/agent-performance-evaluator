from typing import List, Dict, Any, Union, Tuple, Set 
def law_case_get_details(case_number:str, include_history:bool=None, include_litigants:bool=None) -> str:
	"""
	law_case_get_details : Fetches detailed information on a specific case including its history and the litigants involved.    
	Parameters:
	case_number (str): The unique number identifying the case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_history (bool): Flag indicating if case history should be included. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_litigants (bool): Flag indicating if litigant details should be included. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,]

	"""
	return 'Success'

tools = [law_case_get_details]
