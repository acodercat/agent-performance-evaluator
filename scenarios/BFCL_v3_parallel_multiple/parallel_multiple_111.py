from typing import List, Dict, Any, Union, Tuple, Set 
def religion_get_core_beliefs(religion:str) -> str:
	"""
	religion_get_core_beliefs : Retrieves the core beliefs and practices of a specified religion.    
	Parameters:
	religion (str): Name of the religion for which to retrieve the core beliefs and practices.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [religion,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def religion_get_origin(religion:str) -> str:
	"""
	religion_get_origin : Retrieves the origin and founder information of a specified religion.    
	Parameters:
	religion (str): Name of the religion for which to retrieve the founder and origin.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [religion,]

	"""
	return 'Success'

tools = [religion_get_core_beliefs, religion_get_origin]
