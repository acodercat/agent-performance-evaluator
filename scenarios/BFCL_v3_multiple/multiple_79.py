from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_info(location:str, food_type:str=None) -> str:
	"""
	restaurant_info : Get restaurant information for a specific area.    
	Parameters:
	location (str): Location for which to find restaurants.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	food_type (str): Type of cuisine for which to find restaurants. Default 'any'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def exhibition_info(museum_name:str, month:int=None) -> str:
	"""
	exhibition_info : Get exhibition information for a specific museum.    
	Parameters:
	museum_name (str): Name of the museum for which to find exhibitions.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	month (int): Number of upcoming months for which to retrieve exhibition details. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum_name,]

	"""
	return 'Success'

tools = [restaurant_info, exhibition_info]
