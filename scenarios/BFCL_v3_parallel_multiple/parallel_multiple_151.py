def book_hotel(hotel_name, location, room_type, start_date, stay_duration, view='No preference'):
	"""
	Book a room in a specific hotel with particular preferences    
	Parameters:
	hotel_name: The name of the hotel.
	location: The location of the hotel.
	room_type: The type of room preferred.
	start_date: The starting date of the stay in format MM-DD-YYYY.
	stay_duration: The duration of the stay in days.
	view: The preferred view from the room, can be ignored if no preference. If none provided, assumes no preference.

	"""
	pass

def safeway_order(location, items, quantity):
	"""
	Order specified items from a Safeway location.    
	Parameters:
	location: The location of the Safeway store, e.g. Palo Alto, CA.
	items: List of items to order.
	quantity: Quantity of each item in the order list.

	"""
	pass

def latest_exchange_rate(source_currency, target_currency, amount=None):
	"""
	Retrieve the latest exchange rate between two specified currencies.    
	Parameters:
	source_currency: The currency you are converting from.
	target_currency: The currency you are converting to.
	amount: The amount to be converted. If omitted, default to xchange rate of 1 unit source currency.

	"""
	pass

def light_travel_time(distance_in_light_years, speed_of_light=None):
	"""
	Calculate the time taken for light to travel from a celestial body to another.    
	Parameters:
	distance_in_light_years: The distance between the two celestial bodies in light years.
	speed_of_light: The speed of light in vacuum, in m/s. Default value is 299792458 m/s.

	"""
	pass

tools = [book_hotel, safeway_order, latest_exchange_rate, light_travel_time]
