from typing import List, Dict, Any, Union, Tuple, Set 
def poker_probability_full_house(deck_size:int, hand_size:int) -> str:
	"""
	poker_probability_full_house : Calculate the probability of getting a full house in a poker game.    
	Parameters:
	deck_size (int): The size of the deck. Default is 52.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	hand_size (int): The size of the hand. Default is 5.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [deck_size,hand_size,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hospital_locate(location:str, radius:int, department:str=None) -> str:
	"""
	hospital_locate : Locate nearby hospitals based on location and radius. Options to include specific departments are available.    
	Parameters:
	location (str): The city and state, e.g. Denver, CO
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	radius (int): The radius within which you want to find the hospital in kms.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	department (str): Specific department within the hospital. Default is ''.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,radius,]

	"""
	return 'Success'

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

tools = [poker_probability_full_house, hospital_locate, find_recipe]
