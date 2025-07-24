from typing import List, Dict, Any, Union, Tuple, Set 
def get_discoverer(discovery:str, detail:bool):
	"""
	get_discoverer : Get the person or team who made a particular scientific discovery    
	Parameters:
	discovery (str): The discovery for which the discoverer's information is needed.
	detail (bool): Optional flag to get additional details about the discoverer, such as birth date and nationality. Defaults to false.

	Required Parameter = [discovery,detail,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def diabetes_prediction(weight:float, height:float, activity_level:str):
	"""
	diabetes_prediction : Predict the likelihood of diabetes type 2 based on a person's weight and height.    
	Parameters:
	weight (float): Weight of the person in lbs.
	height (float): Height of the person in inches.
	activity_level (str): Physical activity level of the person.

	Required Parameter = [weight,height,activity_level,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def museum_working_hours_get(museum:str, location:str, day:str=None):
	"""
	museum_working_hours_get : Get the working hours of a museum in a specific location.    
	Parameters:
	museum (str): The name of the museum.
	location (str): The location of the museum.
	day (str): Specific day of the week. Optional parameter. Default is 'today'.

	Required Parameter = [museum,location,]

	"""
	return 'Success'

tools = [get_discoverer, diabetes_prediction, museum_working_hours_get]
