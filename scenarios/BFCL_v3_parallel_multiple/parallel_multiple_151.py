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

from typing import List, Dict, Any, Union, Tuple, Set 
def safeway_order(location:str, items:List[str], quantity:List[int]) -> str:
	"""
	safeway_order : Order specified items from a Safeway location.    
	Parameters:
	location (str): The location of the Safeway store, e.g. Palo Alto, CA.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	items (List[str]): List of items to order.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	quantity (List[int]): Quantity of each item in the order list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,items,quantity,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def latest_exchange_rate(source_currency:str, target_currency:str, amount:int=None) -> str:
	"""
	latest_exchange_rate : Retrieve the latest exchange rate between two specified currencies.    
	Parameters:
	source_currency (str): The currency you are converting from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	target_currency (str): The currency you are converting to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (int): The amount to be converted. If omitted, default to xchange rate of 1 unit source currency.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [source_currency,target_currency,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def light_travel_time(distance_in_light_years:float, speed_of_light:int=None) -> str:
	"""
	light_travel_time : Calculate the time taken for light to travel from a celestial body to another.    
	Parameters:
	distance_in_light_years (float): The distance between the two celestial bodies in light years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	speed_of_light (int): The speed of light in vacuum, in m/s. Default value is 299792458 m/s.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [distance_in_light_years,]

	"""
	return 'Success'

tools = [book_hotel, safeway_order, latest_exchange_rate, light_travel_time]
