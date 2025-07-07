def convert_currency(base_currency, target_currency, amount):
	"""
	Converts an amount from a particular currency to another currency.    
	Parameters:
	base_currency: The base currency in which the original amount is present.
	target_currency: The currency to which you want to convert.
	amount: The amount you want to convert.

	"""
	pass

def map_service_get_directions(start, end, avoid=None):
	"""
	Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start: Starting location for the route.
	end: Ending location for the route.
	avoid: Route features to avoid. Default is none if not specified.

	"""
	pass

def ecology_get_turtle_population(location, year=None, species=None):
	"""
	Get the population and species of turtles in a specific location.    
	Parameters:
	location: The name of the location.
	year: The year of the data requested. Default is 2023 if not specified.
	species: Whether to include species information. Default is false. (optional)

	"""
	pass

tools = [convert_currency, map_service_get_directions, ecology_get_turtle_population]
