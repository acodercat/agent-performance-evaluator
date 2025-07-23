from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_info(location:str, food_type:str=None):
	"""
	restaurant_info : Get restaurant information for a specific area.    
	Parameters:
	location (str): Location for which to find restaurants.
	food_type (str): Type of cuisine for which to find restaurants. Default is 'all' if not specified.

	Required Parameter = [location,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def exhibition_info(museum_name:str, month:int=None):
	"""
	exhibition_info : Get exhibition information for a specific museum.    
	Parameters:
	museum_name (str): Name of the museum for which to find exhibitions.
	month (int): Number of upcoming months for which to retrieve exhibition details. Default is 1 if not specified.

	Required Parameter = [museum_name,]

	"""
	pass

tools = [restaurant_info, exhibition_info]
