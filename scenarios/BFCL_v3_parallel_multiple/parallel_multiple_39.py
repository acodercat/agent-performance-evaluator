from typing import List, Dict, Any, Union, Tuple, Set 
def scientist_info_get_birthdate(name:str) -> str:
	"""
	scientist_info_get_birthdate : Retrieve the birthdate of a specific scientist.    
	Parameters:
	name (str): The name of the scientist.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def scientist_info_get_famous_discovery(name:str, discovery_order:int=1) -> str:
	"""
	scientist_info_get_famous_discovery : Retrieve the most famous discovery made by a specific scientist.    
	Parameters:
	name (str): The name of the scientist.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	discovery_order (int): The order of discoveries if the scientist made multiple discoveries. If not provided, the first (or most famous) discovery will be returned.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [name,]

	"""
	return 'Success'

tools = [scientist_info_get_birthdate, scientist_info_get_famous_discovery]
