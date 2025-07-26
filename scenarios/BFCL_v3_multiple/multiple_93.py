from typing import List, Dict, Any, Union, Tuple, Set 
def car_rental(location:str, days:int, car_type:str, pick_up:str=None) -> str:
	"""
	car_rental : Rent a car at the specified location for a specific number of days    
	Parameters:
	location (str): Location of the car rental.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of days for which to rent the car.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	car_type (str): Type of the car to rent.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	pick_up (str): Location of where to pick up the car. Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,days,car_type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_book(location:str, roomType:str, nights:int, additional_services:List[str]=None) -> str:
	"""
	hotel_book : Book a hotel room given the location, room type, and number of nights and additional services    
	Parameters:
	location (str): Location of the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	roomType (str): Type of the room to be booked.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	nights (int): Number of nights to book the room for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	additional_services (List[str]): Additional services to be added. Default empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,roomType,nights,]

	"""
	return 'Success'

tools = [car_rental, hotel_book]
