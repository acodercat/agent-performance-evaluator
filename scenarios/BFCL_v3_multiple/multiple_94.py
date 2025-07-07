def hotel_room_pricing_get(hotelName, roomType, nights):
	"""
	Get pricing for a specific type of hotel room for specified number of nights.    
	Parameters:
	hotelName: The name of the hotel e.g. Hilton New York
	roomType: Type of the room to be booked.
	nights: Number of nights to book the room for.

	"""
	pass

def car_rental_pricing_get(rentalCompany, carType, days):
	"""
	Get pricing for a specific type of rental car for a specified number of days.    
	Parameters:
	rentalCompany: The name of the rental company.
	carType: Type of the car to be rented.
	days: Number of days to rent the car.

	"""
	pass

def flight_ticket_pricing_get(airline, flightClass, passengers):
	"""
	Get pricing for a specific type of flight ticket for specified number of passengers.    
	Parameters:
	airline: The name of the airline.
	flightClass: Class of the flight.
	passengers: Number of passengers.

	"""
	pass

tools = [hotel_room_pricing_get, car_rental_pricing_get, flight_ticket_pricing_get]
