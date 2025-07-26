from typing import List, Dict, Any, Union, Tuple, Set 
def court_info_get_case_status(case_number:str, court:str, details:str=None) -> str:
	"""
	court_info_get_case_status : Retrieves the status and trial dates for court cases from specified county courts.    
	Parameters:
	case_number (str): The specific court case number.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	court (str): The county court where the case is filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	details (str): Specific details required about the court case. Defaults to 'status'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,court,]

	"""
	return 'Success'

tools = [court_info_get_case_status]
