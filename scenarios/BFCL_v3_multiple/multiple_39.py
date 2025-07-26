from typing import List, Dict, Any, Union, Tuple, Set 
def grocery_delivery_order(location:str, items:List[str], max_delivery_cost:float=None) -> str:
	"""
	grocery_delivery_order : Order grocery items from a specific location with optional delivery price limit    
	Parameters:
	location (str): The location of the grocery store
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	items (List[str]): List of items to order
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	max_delivery_cost (float): The maximum delivery cost. It is optional. Default 1000000
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,items,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def ride_hailing_get_rides(source:str, destination:str, max_cost:int=None) -> str:
	"""
	ride_hailing_get_rides : Find ride from source to destination with an optional cost limit    
	Parameters:
	source (str): The starting point of the journey
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): The endpoint of the journey
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	max_cost (int): The maximum cost of the ride. It is optional. Default is 1000000
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [source,destination,]

	"""
	return 'Success'

tools = [grocery_delivery_order, ride_hailing_get_rides]
