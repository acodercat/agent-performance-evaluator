from typing import List, Dict, Any, Union, Tuple, Set 
def map_service_get_directions(start:str, end:str, avoid:List[str]=None) -> str:
	"""
	map_service_get_directions : Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start (str): Starting location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end (str): Ending location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	avoid (List[str]): Route features to avoid. Default is an empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start,end,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def convert_currency(base_currency:str, target_currency:str, amount:int) -> str:
	"""
	convert_currency : Converts an amount from a particular currency to another currency.    
	Parameters:
	base_currency (str): The base currency in which the original amount is present.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	target_currency (str): The currency to which you want to convert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (int): The amount you want to convert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [base_currency,target_currency,amount,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def ecology_get_turtle_population(location:str, year:int=None, species:bool=None) -> str:
	"""
	ecology_get_turtle_population : Get the population and species of turtles in a specific location.    
	Parameters:
	location (str): The name of the location.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year of the data requested. (optional) Default is 2024.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	species (bool): Whether to include species information. Default is false. (optional)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

tools = [map_service_get_directions, convert_currency, ecology_get_turtle_population]
