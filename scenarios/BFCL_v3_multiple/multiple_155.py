from typing import List, Dict, Any, Union, Tuple, Set 
def get_discoverer(discovery:str, detail:bool) -> str:
	"""
	get_discoverer : Get the person or team who made a particular scientific discovery    
	Parameters:
	discovery (str): The discovery for which the discoverer's information is needed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detail (bool): Optional flag to get additional details about the discoverer, such as birth date and nationality. Defaults to false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [discovery,detail,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def diabetes_prediction(weight:float, height:float, activity_level:str) -> str:
	"""
	diabetes_prediction : Predict the likelihood of diabetes type 2 based on a person's weight and height.    
	Parameters:
	weight (float): Weight of the person in lbs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (float): Height of the person in inches.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	activity_level (str): Physical activity level of the person.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [weight,height,activity_level,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def museum_working_hours_get(museum:str, location:str, day:str=None) -> str:
	"""
	museum_working_hours_get : Get the working hours of a museum in a specific location.    
	Parameters:
	museum (str): The name of the museum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location of the museum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	day (str): Specific day of the week. Optional parameter. Default is 'today'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum,location,]

	"""
	return 'Success'

tools = [get_discoverer, diabetes_prediction, museum_working_hours_get]
