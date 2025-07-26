from typing import List, Dict, Any, Union, Tuple, Set 
def map_service_get_directions(start:str, end:str, avoid:List[str]=None) -> str:
	"""
	map_service_get_directions : Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start (str): Starting location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end (str): Ending location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	avoid (List[str]): Route features to avoid. Default is ['highways', 'ferries']
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start,end,]

	"""
	return 'Success'

tools = [map_service_get_directions]
