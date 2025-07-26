from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_booking(location:str, room_type:str, duration:int, start_date:str, preferences:List[str]=None) -> str:
	"""
	hotel_booking : Books a hotel room given the location, room type, stay duration and any additional preferences.    
	Parameters:
	location (str): The city where you want to book the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	room_type (str): Type of the room required. Options: 'single', 'double', 'deluxe', etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (int): The number of nights you want to book the hotel for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	start_date (str): The date when your stay begins.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	preferences (List[str]): Optional preferences of stay at the hotel. Default to use all if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,room_type,duration,start_date,]

	"""
	return 'Success'

tools = [hotel_booking]
