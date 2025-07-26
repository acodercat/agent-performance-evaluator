from typing import List, Dict, Any, Union, Tuple, Set 
def recipe_prep_time(recipe:str) -> str:
	"""
	recipe_prep_time : Calculate the estimated preparation and cooking time for a specified recipe.    
	Parameters:
	recipe (str): Name of the recipe to calculate time for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [recipe,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def recipe_nutrition_info(recipe:str) -> str:
	"""
	recipe_nutrition_info : Provide detailed nutritional information for a specified recipe.    
	Parameters:
	recipe (str): Name of the recipe to fetch nutrition info for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [recipe,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def recipe_search(ingredient:str, dietary_requirements:List[str], isHomemade:bool) -> str:
	"""
	recipe_search : Search for a recipe based on a particular ingredient or dietary requirement.    
	Parameters:
	ingredient (str): The ingredient that you want to have in the recipe.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dietary_requirements (List[str]): Dietary requirements in the recipe.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	isHomemade (bool): If true, returns homemade recipe; otherwise, return not homemade recipe.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [ingredient,dietary_requirements,isHomemade,]

	"""
	return 'Success'

tools = [recipe_prep_time, recipe_nutrition_info, recipe_search]
