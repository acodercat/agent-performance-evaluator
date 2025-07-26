from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_search(entity:str, county:str, state:str=None) -> str:
	"""
	lawsuit_search : Retrieve all lawsuits involving a particular entity from specified jurisdiction.    
	Parameters:
	entity (str): The entity involved in lawsuits.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	county (str): The jurisdiction for the lawsuit search for example Alameda county.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	state (str): The state for the lawsuit search. Default is California.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [entity,county,]

	"""
	return 'Success'

tools = [lawsuit_search]
