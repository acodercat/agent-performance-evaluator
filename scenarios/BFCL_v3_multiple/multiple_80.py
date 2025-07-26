from typing import List, Dict, Any, Union, Tuple, Set 
def music_shop_find_nearby(location:str, services:List[str]=None, instruments:List[str]=None) -> str:
	"""
	music_shop_find_nearby : Locate nearby music shops based on specific criteria like instrument lessons availability.    
	Parameters:
	location (str): The city and state, e.g. Nashville, TN
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	services (List[str]): Types of instrument lessons offered in the shop. Default empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	instruments (List[str]): Types of instruments sold in the shop. Default empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def gym_find_nearby(location:str, classes:List[str]=None, equipment:List[str]=None) -> str:
	"""
	gym_find_nearby : Locate nearby gyms based on specific criteria like types of fitness classes availability.    
	Parameters:
	location (str): The city and state, e.g. Nashville, TN
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	classes (List[str]): Types of fitness classes offered in the gym. Default empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	equipment (List[str]): Types of gym equipment available. Default empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

tools = [music_shop_find_nearby, gym_find_nearby]
