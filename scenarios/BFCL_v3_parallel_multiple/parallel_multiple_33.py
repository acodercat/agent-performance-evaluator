from typing import List, Dict, Any, Union, Tuple 
def supermarket_find_in_city(city:str, state:str, openNow:bool=None):
	"""
	supermarket_find_in_city : Find all supermarkets in a given city.    
	Parameters:
	city (str): The city to locate supermarkets in.
	state (str): The state to further narrow down the search.
	openNow (bool): If true, returns only supermarkets that are currently open. Default to true

	Required Parameter = [city,state,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def sightseeing_popular_in_city(city:str, state:str, kidsFriendly:bool=None):
	"""
	sightseeing_popular_in_city : Find the most popular sightseeing place in a given city.    
	Parameters:
	city (str): The city to find sightseeing in.
	state (str): The state to further narrow down the search.
	kidsFriendly (bool): If true, returns only kids friendly sightseeing places.Default to true

	Required Parameter = [city,state,]

	"""
	pass

tools = [supermarket_find_in_city, sightseeing_popular_in_city]
