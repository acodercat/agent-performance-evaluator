from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_search(location:str, cuisine:str, rating:float=None) -> str:
	"""
	restaurant_search : Find a restaurant in a specified location based on the cuisine and ratings.    
	Parameters:
	location (str): The city and state, e.g. New York, NY
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cuisine (str): The type of cuisine.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rating (float): The minimum rating. Default 1.0
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,cuisine,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def flight_search(_from:str, to:str, type:str) -> str:
	"""
	flight_search : Find flights between two cities.    
	Parameters:
	_from (str): The departure city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to (str): The destination city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): The type of flight e.g., one-way, round-trip
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [_from,to,type,]

	"""
	return 'Success'

tools = [restaurant_search, flight_search]
