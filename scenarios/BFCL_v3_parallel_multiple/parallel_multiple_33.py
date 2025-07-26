from typing import List, Dict, Any, Union, Tuple, Set 
def supermarket_find_in_city(city:str, state:str, openNow:bool=None) -> str:
	"""
	supermarket_find_in_city : Find all supermarkets in a given city.    
	Parameters:
	city (str): The city to locate supermarkets in.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	state (str): The state to further narrow down the search.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	openNow (bool): If true, returns only supermarkets that are currently open. Default to true
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city,state,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sightseeing_popular_in_city(city:str, state:str, kidsFriendly:bool=None) -> str:
	"""
	sightseeing_popular_in_city : Find the most popular sightseeing place in a given city.    
	Parameters:
	city (str): The city to find sightseeing in.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	state (str): The state to further narrow down the search.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	kidsFriendly (bool): If true, returns only kids friendly sightseeing places.Default to true
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city,state,]

	"""
	return 'Success'

tools = [supermarket_find_in_city, sightseeing_popular_in_city]
