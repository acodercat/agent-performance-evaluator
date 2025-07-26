from typing import List, Dict, Any, Union, Tuple, Set 
def get_recipe(dish_name:str, diet_preference:str='none') -> str:
	"""
	get_recipe : Fetch the recipe for a specific dish along with preparation steps.    
	Parameters:
	dish_name (str): Name of the dish whose recipe needs to be fetched.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	diet_preference (str): Preferred dietary consideration like vegan, vegetarian, gluten-free etc. Default is none.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [dish_name,]

	"""
	return 'Success'

tools = [get_recipe]
