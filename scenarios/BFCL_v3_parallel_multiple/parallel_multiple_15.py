from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_search(location:str, cuisine:str, rating:float=None):
	"""
	restaurant_search : Find a restaurant in a specified location based on the cuisine and ratings.    
	Parameters:
	location (str): The city and state, e.g. New York, NY
	cuisine (str): The type of cuisine.
	rating (float): The minimum rating. Default 1.0

	Required Parameter = [location,cuisine,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def flight_search(_from:str, to:str, type:str):
	"""
	flight_search : Find flights between two cities.    
	Parameters:
	_from (str): The departure city.
	to (str): The destination city.
	type (str): The type of flight e.g., one-way, round-trip

	Required Parameter = [_from,to,type,]

	"""
	pass

tools = [restaurant_search, flight_search]
