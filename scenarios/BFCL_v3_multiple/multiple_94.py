from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_room_pricing_get(hotelName:str, roomType:str, nights:int) -> str:
	"""
	hotel_room_pricing_get : Get pricing for a specific type of hotel room for specified number of nights.    
	Parameters:
	hotelName (str): The name of the hotel e.g. Hilton New York
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	roomType (str): Type of the room to be booked.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	nights (int): Number of nights to book the room for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [hotelName,roomType,nights,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def car_rental_pricing_get(rentalCompany:str, carType:str, days:int) -> str:
	"""
	car_rental_pricing_get : Get pricing for a specific type of rental car for a specified number of days.    
	Parameters:
	rentalCompany (str): The name of the rental company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	carType (str): Type of the car to be rented.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of days to rent the car.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [rentalCompany,carType,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def flight_ticket_pricing_get(airline:str, flightClass:str, passengers:int) -> str:
	"""
	flight_ticket_pricing_get : Get pricing for a specific type of flight ticket for specified number of passengers.    
	Parameters:
	airline (str): The name of the airline.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	flightClass (str): Class of the flight.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	passengers (int): Number of passengers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [airline,flightClass,passengers,]

	"""
	return 'Success'

tools = [hotel_room_pricing_get, car_rental_pricing_get, flight_ticket_pricing_get]
