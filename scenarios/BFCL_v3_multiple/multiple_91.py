from typing import List, Dict, Any, Union, Tuple 
def restaurant_find(cuisine:str, price:List[str]=None):
	"""
	restaurant_find : Locate restaurants based on specific criteria such as cuisine and price range    
	Parameters:
	cuisine (str): The type of cuisine preferred.
	price (List[str]): Price range of the restaurant in format ['low', 'mid', 'high']. Default ['low', 'mid', 'high']

	Required Parameter = [cuisine,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def recipe_find(mainIngredient:str, ingredientLimit:int):
	"""
	recipe_find : Locate cooking recipes based on specific criteria such as main ingredient and number of ingredients    
	Parameters:
	mainIngredient (str): Main ingredient for the recipe.
	ingredientLimit (int): Max number of ingredients the recipe should use.

	Required Parameter = [mainIngredient,ingredientLimit,]

	"""
	pass

tools = [restaurant_find, recipe_find]
