from typing import List, Dict, Any, Union, Tuple, Set 
def criminal_record_get_offense_nature(criminal_name:str, optional_param:bool=None) -> str:
	"""
	criminal_record_get_offense_nature : Get details about the nature of offenses committed by a criminal.    
	Parameters:
	criminal_name (str): Name of the criminal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	optional_param (bool): Optionally retrieve additional details, by default this is set to false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [criminal_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def criminal_record_get_status(criminal_name:str, region:str) -> str:
	"""
	criminal_record_get_status : Find the conviction status of a criminal in a specified region.    
	Parameters:
	criminal_name (str): Name of the criminal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): Region where criminal record is to be searched.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [criminal_name,region,]

	"""
	return 'Success'

tools = [criminal_record_get_offense_nature, criminal_record_get_status]
