from typing import List, Dict, Any, Union, Tuple, Set 
def tourist_spot_info(spot:str, city:str, details:List[str]='timing, attractions') -> str:
	"""
	tourist_spot_info : Retrieve information about a specific tourist spot.    
	Parameters:
	spot (str): The name of the tourist spot you want to get information for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city where the tourist spot is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	details (List[str]): Details of the tourist spot to get information on. For multiple details, separate them by comma.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [spot,city,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def museum_info(museum:str, city:str, features:List[str]='timings, exhibitions') -> str:
	"""
	museum_info : Retrieve information about a specific museum.    
	Parameters:
	museum (str): The name of the museum you want to get information for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city where the museum is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	features (List[str]): Features of the museum to get information on. For multiple features, separate them by comma.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum,city,]

	"""
	return 'Success'

tools = [tourist_spot_info, museum_info]
