def events_find_event(location, group_size, event_type=None):
	"""
	Find events suitable for groups based on specified criteria such as location and event type.    
	Parameters:
	location: The city and state, e.g. Seattle, WA
	event_type: Type of event. Default empty array
	group_size: Size of the group that the event should accommodate.

	"""
	pass

def restaurant_find_group(location, group_size, cuisine=None):
	"""
	Find restaurants suitable for groups based on specified criteria such as location and cuisine.    
	Parameters:
	location: The city and state, e.g. Seattle, WA
	cuisine: Preferred cuisine at the restaurant. Default empty array
	group_size: Size of the group that the restaurant should accommodate.

	"""
	pass

tools = [events_find_event, restaurant_find_group]
