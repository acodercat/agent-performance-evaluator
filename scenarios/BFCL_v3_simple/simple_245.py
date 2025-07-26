from typing import List, Dict, Any, Union, Tuple, Set 
def discoverer_get(element_name:str, year:int=None, first:bool=True) -> str:
	"""
	discoverer_get : Retrieve the name of the discoverer of an element based on its name.    
	Parameters:
	element_name (str): The name of the element.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Optional parameter that refers to the year of discovery. It could be helpful in case an element was discovered more than once. Default to 0, which means not use it.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	first (bool): Optional parameter indicating if the first discoverer's name should be retrieved.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [element_name,]

	"""
	return 'Success'

tools = [discoverer_get]
