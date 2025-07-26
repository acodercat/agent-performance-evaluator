from typing import List, Dict, Any, Union, Tuple, Set 
def geometry_area_circle(radius:float, units:str='meters') -> str:
	"""
	geometry_area_circle : Calculate the area of a circle given the radius.    
	Parameters:
	radius (float): The radius of the circle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	units (str): The units in which the radius is measured (defaults to meters).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [radius,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def find_recipes(diet:str, meal_type:str, ingredients:List[str]=None) -> str:
	"""
	find_recipes : Find recipes based on dietary restrictions, meal type, and preferred ingredients.    
	Parameters:
	diet (str): The dietary restrictions, e.g., 'vegan', 'gluten-free'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	meal_type (str): The type of meal, e.g., 'dinner', 'breakfast'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	ingredients (List[str]): The preferred ingredients. If left blank, it will return general recipes. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [diet,meal_type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def whole_foods_check_price(location:str, items:List[str]) -> str:
	"""
	whole_foods_check_price : Check the price of items at a specific Whole Foods location.    
	Parameters:
	location (str): Location of the Whole Foods store.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	items (List[str]): List of items for which the price needs to be checked.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,items,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_shortest_distance(start_location:str, end_location:str, route_preference:str) -> str:
	"""
	calculate_shortest_distance : Calculate the shortest driving distance between two locations.    
	Parameters:
	start_location (str): The starting location for the drive.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end_location (str): The destination location for the drive.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	route_preference (str): The preferred type of route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start_location,end_location,route_preference,]

	"""
	return 'Success'

tools = [geometry_area_circle, find_recipes, whole_foods_check_price, calculate_shortest_distance]
