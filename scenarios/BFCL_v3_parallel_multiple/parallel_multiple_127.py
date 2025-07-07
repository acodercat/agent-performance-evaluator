def car_rental(location, days, car_type, pick_up=None):
	"""
	Rent a car at the specified location for a specific number of days    
	Parameters:
	location: Location of the car rental.
	days: Number of days for which to rent the car.
	car_type: Type of the car to rent.
	pick_up: Location of where to pick up the car. Default is 'airport' if not specified.

	"""
	pass

def hotel_book(location, roomType, nights, additional_services=None):
	"""
	Book a hotel room given the location, room type, and number of nights and additional services    
	Parameters:
	location: Location of the hotel.
	roomType: Type of the room to be booked.
	nights: Number of nights to book the room for.
	additional_services: Additional services to be added. Default is not use it if not specified.

	"""
	pass

tools = [car_rental, hotel_book]
