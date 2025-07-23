from typing import List, Dict, Any, Union, Tuple, Set 
def flight_ticket_pricing_get(airline:str, flightClass:str, passengers:int):
	"""
	flight_ticket_pricing_get : Get pricing for a specific type of flight ticket for specified number of passengers.    
	Parameters:
	airline (str): The name of the airline.
	flightClass (str): Class of the flight.
	passengers (int): Number of passengers.

	Required Parameter = [airline,flightClass,passengers,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def car_rental_pricing_get(rentalCompany:str, carType:str, days:int):
	"""
	car_rental_pricing_get : Get pricing for a specific type of rental car for a specified number of days.    
	Parameters:
	rentalCompany (str): The name of the rental company.
	carType (str): Type of the car to be rented.
	days (int): Number of days to rent the car.

	Required Parameter = [rentalCompany,carType,days,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_room_pricing_get(hotelName:str, roomType:str, nights:int):
	"""
	hotel_room_pricing_get : Get pricing for a specific type of hotel room for specified number of nights.    
	Parameters:
	hotelName (str): The name of the hotel e.g. Hilton New York
	roomType (str): Type of the room to be booked.
	nights (int): Number of nights to book the room for.

	Required Parameter = [hotelName,roomType,nights,]

	"""
	pass

tools = [flight_ticket_pricing_get, car_rental_pricing_get, hotel_room_pricing_get]
