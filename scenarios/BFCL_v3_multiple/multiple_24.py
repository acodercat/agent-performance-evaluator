from typing import List, Dict, Any, Union, Tuple, Set 
def route_planner_calculate_route(start:str, destination:str, method:str='fastest') -> str:
	"""
	route_planner_calculate_route : Determines the best route between two points.    
	Parameters:
	start (str): The starting point of the journey.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): The destination of the journey.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	method (str): The method to use when calculating the route (default is 'fastest').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start,destination,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def chess_club_details_find(name:str, city:str, event:str='null') -> str:
	"""
	chess_club_details_find : Provides details about a chess club, including location.    
	Parameters:
	name (str): The name of the chess club.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city in which the chess club is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	event (str): The event hosted by the club.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [name,city,]

	"""
	return 'Success'

tools = [route_planner_calculate_route, chess_club_details_find]
