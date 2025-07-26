from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_find(location:str, stars:int, amenities:List[str]=None) -> str:
	"""
	hotel_find : Search for hotels given the location, minimum stars and specific amenities.    
	Parameters:
	location (str): The city where you want to find the hotel
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	stars (int): Minimum number of stars the hotel should have. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amenities (List[str]): List of preferred amenities in hotel. Default to empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,stars,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def flight_search(origin:str, destination:str, date:Any=None, passengers:int=1) -> str:
	"""
	flight_search : Search for flights given the origin, destination, date, and number of passengers.    
	Parameters:
	origin (str): The origin of the flight
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): The destination of the flight
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (Any): The date of the flight. Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	passengers (int): The number of passengers
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [origin,destination,]

	"""
	return 'Success'

tools = [hotel_find, flight_search]
