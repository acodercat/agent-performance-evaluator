def flights_search(from_city, to_city, date=None):
	"""
	Find flights between two cities.    
	Parameters:
	from_city: The city to depart from.
	to_city: The city to arrive at.
	date: The date to fly. Default is today if not specified.

	"""
	pass

def timezones_get_difference(city1, city2):
	"""
	Find the time difference between two cities.    
	Parameters:
	city1: The first city.
	city2: The second city.

	"""
	pass

def geodistance_find(origin, destination, unit='miles'):
	"""
	Find the distance between two cities on the globe.    
	Parameters:
	origin: The originating city for the distance calculation.
	destination: The destination city for the distance calculation.
	unit: The unit of measure for the distance calculation.

	"""
	pass

tools = [flights_search, timezones_get_difference, geodistance_find]
