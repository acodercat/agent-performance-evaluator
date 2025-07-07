def get_discoverer(discovery, detail):
	"""
	Get the person or team who made a particular scientific discovery    
	Parameters:
	discovery: The discovery for which the discoverer's information is needed.
	detail: Optional flag to get additional details about the discoverer, such as birth date and nationality. Defaults to false.

	"""
	pass

def museum_working_hours_get(museum, location, day=None):
	"""
	Get the working hours of a museum in a specific location.    
	Parameters:
	museum: The name of the museum.
	location: The location of the museum.
	day: Specific day of the week. Optional parameter. Default is 'Monday'.

	"""
	pass

def diabetes_prediction(weight, height, activity_level):
	"""
	Predict the likelihood of diabetes type 2 based on a person's weight and height.    
	Parameters:
	weight: Weight of the person in lbs.
	height: Height of the person in inches.
	activity_level: Physical activity level of the person.

	"""
	pass

tools = [get_discoverer, museum_working_hours_get, diabetes_prediction]
