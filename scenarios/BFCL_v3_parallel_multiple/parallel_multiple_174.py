from typing import List, Dict, Any, Union, Tuple, Set 
def convert_currency(base_currency:str, target_currency:str, amount:int):
	"""
	convert_currency : Converts an amount from a particular currency to another currency.    
	Parameters:
	base_currency (str): The base currency in which the original amount is present.
	target_currency (str): The currency to which you want to convert.
	amount (int): The amount you want to convert.

	Required Parameter = [base_currency,target_currency,amount,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def map_service_get_directions(start:str, end:str, avoid:List[str]=None):
	"""
	map_service_get_directions : Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start (str): Starting location for the route.
	end (str): Ending location for the route.
	avoid (List[str]): Route features to avoid. Default is none if not specified.

	Required Parameter = [start,end,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def ecology_get_turtle_population(location:str, year:int=None, species:bool=None):
	"""
	ecology_get_turtle_population : Get the population and species of turtles in a specific location.    
	Parameters:
	location (str): The name of the location.
	year (int): The year of the data requested. Default is 2023 if not specified.
	species (bool): Whether to include species information. Default is false. (optional)

	Required Parameter = [location,]

	"""
	return 'Success'

tools = [convert_currency, map_service_get_directions, ecology_get_turtle_population]
