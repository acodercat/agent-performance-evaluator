from typing import List, Dict, Any, Union, Tuple, Set 
def get_vegan_recipe(dish_type:str, cooking_time:int, ingredient_preference:List[str]=None) -> str:
	"""
	get_vegan_recipe : Retrieve a vegan soup recipe based on the provided cooking time.    
	Parameters:
	dish_type (str): The type of dish, e.g. soup, dessert, etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cooking_time (int): The maximum cooking time for the recipe in minutes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	ingredient_preference (List[str]): Preferred ingredients to be included in the recipe, if any. Default to not use it if not provided.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [dish_type,cooking_time,]

	"""
	return 'Success'

tools = [get_vegan_recipe]
