from typing import List, Dict, Any, Union, Tuple, Set 
def legal_case_fetch(case_id:str, details:bool) -> str:
	"""
	legal_case_fetch : Fetch detailed legal case information from database.    
	Parameters:
	case_id (str): The ID of the legal case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	details (bool): True if need the detail info. 
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_id,details,]

	"""
	return 'Success'

tools = [legal_case_fetch]
