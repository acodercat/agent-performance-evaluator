from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_find(cuisine:str, price:List[str]=None) -> str:
	"""
	restaurant_find : Locate restaurants based on specific criteria such as cuisine and price range    
	Parameters:
	cuisine (str): The type of cuisine preferred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	price (List[str]): Price range of the restaurant in format ['low', 'mid', 'high']. Default is 'mid' if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [cuisine,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def recipe_find(mainIngredient:str, ingredientLimit:int) -> str:
	"""
	recipe_find : Locate cooking recipes based on specific criteria such as main ingredient and number of ingredients    
	Parameters:
	mainIngredient (str): Main ingredient for the recipe.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	ingredientLimit (int): Max number of ingredients the recipe should use.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [mainIngredient,ingredientLimit,]

	"""
	return 'Success'

tools = [restaurant_find, recipe_find]
