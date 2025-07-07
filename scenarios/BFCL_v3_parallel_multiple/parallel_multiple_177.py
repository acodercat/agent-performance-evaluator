def get_sculpture_value(sculpture, artist):
	"""
	Retrieve the current market value of a particular sculpture by a specific artist.    
	Parameters:
	sculpture: The name of the sculpture.
	artist: The name of the artist who created the sculpture.

	"""
	pass

def history_get_key_events(country, start_year, end_year, event_type=None):
	"""
	Retrieve key historical events within a specific period for a certain country.    
	Parameters:
	country: The name of the country for which history is queried.
	start_year: Start year of the period for which history is queried.
	end_year: End year of the period for which history is queried.
	event_type: Types of event. If none is provided, default that all types will be considered.

	"""
	pass

tools = [get_sculpture_value, history_get_key_events]
