from typing import List, Dict, Any, Union, Tuple, Set 
def court_case_search(docket_number:str, location:str, full_text:bool='false') -> str:
	"""
	court_case_search : Retrieves details about a court case using its docket number and location.    
	Parameters:
	docket_number (str): The docket number for the case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location where the case is registered, in the format: state, e.g., Texas
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	full_text (bool): Option to return the full text of the case ruling.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [docket_number,location,]

	"""
	return 'Success'

tools = [court_case_search]
