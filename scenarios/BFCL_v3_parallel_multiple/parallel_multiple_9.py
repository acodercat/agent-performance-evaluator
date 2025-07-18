from typing import List, Dict, Any, Union, Tuple 
def flight_book(_from:str, to:str, airlines:str):
	"""
	flight_book : Book a flight for a specific route and airlines    
	Parameters:
	_from (str): The departure city in full name.
	to (str): The arrival city in full name.
	airlines (str): The preferred airline.

	Required Parameter = [_from,to,airlines,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def hotel_book(location:str, nights:int):
	"""
	hotel_book : Book a hotel for a specific location for the number of nights    
	Parameters:
	location (str): The city where the hotel is located.
	nights (int): Number of nights for the stay.

	Required Parameter = [location,nights,]

	"""
	pass

tools = [flight_book, hotel_book]
