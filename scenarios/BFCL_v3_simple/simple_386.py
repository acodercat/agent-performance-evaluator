from typing import List, Dict, Any, Union, Tuple, Set 
def book_hotel(hotel_name:str, location:str, room_type:str, start_date:str, stay_duration:int, view:str='No preference') -> str:
	"""
	book_hotel : Book a room in a specific hotel with particular preferences    
	Parameters:
	hotel_name (str): The name of the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location of the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	room_type (str): The type of room preferred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	start_date (str): The starting date of the stay in format MM-DD-YYYY.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	stay_duration (int): The duration of the stay in days.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	view (str): The preferred view from the room, can be ignored if no preference. If none provided, assumes no preference.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [hotel_name,location,room_type,start_date,stay_duration,]

	"""
	return 'Success'

tools = [book_hotel]
