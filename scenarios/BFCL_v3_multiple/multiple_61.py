from typing import List, Dict, Any, Union, Tuple, Set 
def home_renovation_expert_find_specialty(location:str, specialization:str, years_experience:int=0) -> str:
	"""
	home_renovation_expert_find_specialty : Search for a home renovation expert based on the location and specialization    
	Parameters:
	location (str): City and state where the professional is based, e.g. Portland, OR.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specialization (str): A specific area of expertise, such as kitchen or bathroom renovation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	years_experience (int): Number of years the professional has been practicing in their field. (optional)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,specialization,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def landscape_architect_find_specialty(location:str, specialization:str, years_experience:int=0) -> str:
	"""
	landscape_architect_find_specialty : Search for a landscape architect based on the location and specialization    
	Parameters:
	location (str): City and state where the professional is based, e.g. Portland, OR.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specialization (str): A specific area of expertise. Common areas include residential design, commercial design, urban design, and park design.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	years_experience (int): Number of years the professional has been practicing in their field. (optional)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,specialization,]

	"""
	return 'Success'

tools = [home_renovation_expert_find_specialty, landscape_architect_find_specialty]
