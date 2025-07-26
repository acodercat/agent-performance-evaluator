from typing import List, Dict, Any, Union, Tuple, Set 
def find_recipe(dietary_restrictions:str, recipe_type:str, time:int) -> str:
	"""
	find_recipe : Find a recipe based on the dietary restrictions, recipe type, and time constraints.    
	Parameters:
	dietary_restrictions (str): Dietary restrictions e.g. vegan, vegetarian, gluten free, dairy free.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	recipe_type (str): Type of the recipe. E.g. dessert, main course, breakfast.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): Time limit in minutes to prep the meal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [dietary_restrictions,recipe_type,time,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def science_history_get_discovery_details(discovery:str, method_used:str=None) -> str:
	"""
	science_history_get_discovery_details : Retrieve the details of a scientific discovery based on the discovery name.    
	Parameters:
	discovery (str): The name of the discovery, e.g. Gravity
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	method_used (str): The method used for the discovery, default value is 'default' which gives the most accepted method.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [discovery,]

	"""
	return 'Success'

tools = [find_recipe, science_history_get_discovery_details]
