from typing import List, Dict, Any, Union, Tuple, Set 
def create_player_profile(player_name:str, _class:str, starting_level:int=1) -> str:
	"""
	create_player_profile : Create a new player profile with character name, class and starting level.    
	Parameters:
	player_name (str): The desired name of the player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	_class (str): The character class for the player
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	starting_level (int): The starting level for the player
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,_class,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def walmart_purchase(loc:str, product_list:List[str], pack_size:List[int]=None) -> str:
	"""
	walmart_purchase : Retrieve information of items from Walmart including stock availability.    
	Parameters:
	loc (str): Location of the nearest Walmart.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	product_list (List[str]): Items to be purchased listed in an array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	pack_size (List[int]): Size of the product pack if applicable. The size of the array should be equal to product_list. Default is an empty array
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [loc,product_list,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def mutation_type_find(snp_id:str, species:str=None) -> str:
	"""
	mutation_type_find : Finds the type of a genetic mutation based on its SNP (Single Nucleotide Polymorphism) ID.    
	Parameters:
	snp_id (str): The ID of the Single Nucleotide Polymorphism (SNP) mutation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	species (str): Species in which the SNP occurs, default is 'Homo sapiens' (Humans).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [snp_id,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def find_restaurants(location:str, food_type:str, number:int, dietary_requirements:List[str]='None') -> str:
	"""
	find_restaurants : Locate nearby restaurants based on location and food preferences.    
	Parameters:
	location (str): The specific location or area.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	food_type (str): The type of food preferred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number (int): Number of results to return.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dietary_requirements (List[str]): Special dietary requirements, e.g. vegan, gluten-free.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,food_type,number,]

	"""
	return 'Success'

tools = [create_player_profile, walmart_purchase, mutation_type_find, find_restaurants]
