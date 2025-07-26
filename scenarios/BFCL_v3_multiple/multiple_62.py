from typing import List, Dict, Any, Union, Tuple, Set 
def nature_park_find_nearby(location:str, features:List[str]) -> str:
	"""
	nature_park_find_nearby : Locate nearby nature parks based on specific criteria like camping availability and scenic views.    
	Parameters:
	location (str): The city and state, e.g. Boston, MA.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	features (List[str]): Preferred features in nature park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,features,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_find_nearby(location:str, amenities:List[str]=None) -> str:
	"""
	restaurant_find_nearby : Locate nearby restaurants based on specific criteria.    
	Parameters:
	location (str): The city and state, e.g. Boston, MA.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amenities (List[str]): Preferred amenities in restaurant. Default empty array []
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

tools = [nature_park_find_nearby, restaurant_find_nearby]
