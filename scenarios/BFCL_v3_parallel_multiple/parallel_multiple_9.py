from typing import List, Dict, Any, Union, Tuple, Set 
def flight_book(_from:str, to:str, airlines:str) -> str:
	"""
	flight_book : Book a flight for a specific route and airlines    
	Parameters:
	_from (str): The departure city in full name.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to (str): The arrival city in full name.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	airlines (str): The preferred airline.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [_from,to,airlines,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_book(location:str, nights:int) -> str:
	"""
	hotel_book : Book a hotel for a specific location for the number of nights    
	Parameters:
	location (str): The city where the hotel is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	nights (int): Number of nights for the stay.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,nights,]

	"""
	return 'Success'

tools = [flight_book, hotel_book]
