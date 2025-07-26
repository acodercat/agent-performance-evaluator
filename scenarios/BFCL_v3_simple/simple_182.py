from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_info(case_number:str, year:int=2023, location:str=None) -> str:
	"""
	lawsuit_info : Retrieves details of a lawsuit given a case number    
	Parameters:
	case_number (str): The unique identifier of the lawsuit case
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year in which the lawsuit case was initiated. Default is 2023 if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location or court jurisdiction where the case was filed. Default is 'all'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,]

	"""
	return 'Success'

tools = [lawsuit_info]
