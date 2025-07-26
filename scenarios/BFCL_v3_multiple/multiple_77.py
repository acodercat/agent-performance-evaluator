from typing import List, Dict, Any, Union, Tuple, Set 
def tourist_attraction_find(attractionType:str, location:str) -> str:
	"""
	tourist_attraction_find : Search for tourist attractions based on type and location.    
	Parameters:
	attractionType (str): Type of the attraction. E.g., monument, museum, park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Location or city where the attraction is.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [attractionType,location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def artwork_search_find(type:str, location:str, era:str=None) -> str:
	"""
	artwork_search_find : Search for artworks based on type and location.    
	Parameters:
	type (str): Type of the artwork. E.g., painting, sculpture, installation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Location or city where the artwork is.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	era (str): Time period of the artwork, can be 'contemporary', 'modern', 'renaissance', etc. Default 'contemporary'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [type,location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def park_search_find(facilities:List[str], location:str) -> str:
	"""
	park_search_find : Search for parks based on facilities and location.    
	Parameters:
	facilities (List[str]): List of facilities in the park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Location or city where the park is.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [facilities,location,]

	"""
	return 'Success'

tools = [tourist_attraction_find, artwork_search_find, park_search_find]
