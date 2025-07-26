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
	preferences (List[str]): Optional preferences of stay at the hotel. Default is all if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,room_type,duration,start_date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def soccer_get_last_match(team_name:str, include_stats:bool=None) -> str:
	"""
	soccer_get_last_match : Retrieve the details of the last match played by a specified soccer club.    
	Parameters:
	team_name (str): The name of the soccer club.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_stats (bool): If true, include match statistics like possession, shots on target etc. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_BMI(weight_kg:int, height_m:float) -> str:
	"""
	calculate_BMI : Calculate the Body Mass Index (BMI) given a person's weight and height.    
	Parameters:
	weight_kg (int): The weight of the person in kilograms.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height_m (float): The height of the person in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [weight_kg,height_m,]

	"""
	return 'Success'

tools = [hotel_booking, soccer_get_last_match, calculate_BMI]
