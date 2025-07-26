from typing import List, Dict, Any, Union, Tuple, Set 
def crime_record_get_record(case_number:str, county:str, details:bool=None) -> str:
	"""
	crime_record_get_record : Retrieve detailed felony crime records using a specific case number and location.    
	Parameters:
	case_number (str): The case number related to the crime.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	county (str): The county in which the crime occurred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	details (bool): To get a detailed report, set as true. Defaults to false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,county,]

	"""
	return 'Success'

tools = [crime_record_get_record]
