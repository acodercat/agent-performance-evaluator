from typing import List, Dict, Any, Union, Tuple, Set 
def get_lawsuit_details(case_number:str, court_location:str, with_verdict:bool=None) -> str:
	"""
	get_lawsuit_details : Retrieve details of a lawsuit based on its case number and court location.    
	Parameters:
	case_number (str): Case number of the lawsuit.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	court_location (str): The location of the court where the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	with_verdict (bool): Flag to include verdict details if available. Default is False
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,court_location,]

	"""
	return 'Success'

tools = [get_lawsuit_details]
