from typing import List, Dict, Any, Union, Tuple, Set 
def species_distribution_modeling_project_range_shift(species:str, climate_scenario:str, future_time:int=100) -> str:
	"""
	species_distribution_modeling_project_range_shift : Predict the potential future geographic distribution of a species under a specified climate change scenario.    
	Parameters:
	species (str): The species of animal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	climate_scenario (str): The name of the climate change scenario.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	future_time (int): The future time in years for the prediction.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [species,climate_scenario,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def population_genetics_calculate_ne(species:str, generations:int, probability:float) -> str:
	"""
	population_genetics_calculate_ne : Calculate the effective population size necessary to maintain genetic diversity in a wild animal population for a specified number of generations with a given probability.    
	Parameters:
	species (str): The species of wild animal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	generations (int): The number of generations for which to maintain the genetic diversity.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	probability (float): The probability of maintaining genetic diversity.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [species,generations,probability,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def ecology_calculate_carrying_capacity(habitat_area:float, species:str, productivity:float) -> str:
	"""
	ecology_calculate_carrying_capacity : Calculate the maximum population size of the species that the environment can sustain indefinitely.    
	Parameters:
	habitat_area (float): The area of the habitat in square kilometers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	species (str): The species of animal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	productivity (float): The biological productivity of the habitat in animals per square kilometer per year.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [habitat_area,species,productivity,]

	"""
	return 'Success'

tools = [species_distribution_modeling_project_range_shift, population_genetics_calculate_ne, ecology_calculate_carrying_capacity]
