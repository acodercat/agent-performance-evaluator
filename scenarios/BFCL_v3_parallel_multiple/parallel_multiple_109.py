def european_history_get_events(country, century, event_type=None):
	"""
	Provides a list of major historical events based on the specified country and century.    
	Parameters:
	country: Country name.
	century: Century as an integer. For example, for the 1700s, input '18'.
	event_type: Type of the event such as 'war', 'invention', 'revolution' etc. This field is optional. Default to 'war'.

	"""
	pass

def european_history_get_monarchs(country, century):
	"""
	Provides a list of monarchs based on the specified country and century.    
	Parameters:
	country: Country name.
	century: Century as an integer. For example, for the 1700s, input '18'.

	"""
	pass

def european_history_get_culture(country, century, aspect=None):
	"""
	Provides information on cultural trends, art movements, philosophical ideas based on the specified country and century.    
	Parameters:
	country: Country name.
	century: Century as an integer. For example, for the 1700s, input '18'.
	aspect: Aspect of culture such as 'literature', 'art', 'philosophy' etc. This field is optional. Default to 'art'.

	"""
	pass

tools = [european_history_get_events, european_history_get_monarchs, european_history_get_culture]
