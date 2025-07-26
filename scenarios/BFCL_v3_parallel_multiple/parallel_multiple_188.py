from typing import List, Dict, Any, Union, Tuple, Set 
def sports_ranking_get_top_player(sport:str, gender:str='men') -> str:
	"""
	sports_ranking_get_top_player : Get the top player in a specific sport.    
	Parameters:
	sport (str): The type of sport.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	gender (str): The gender of the sport category. Optional.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [sport,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def electromagnetic_force(charge1:int, charge2:int, distance:float, medium_permittivity:float=None) -> str:
	"""
	electromagnetic_force : Calculate the electromagnetic force between two charges placed at a certain distance.    
	Parameters:
	charge1 (int): The magnitude of the first charge in coulombs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	charge2 (int): The magnitude of the second charge in coulombs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	distance (float): The distance between the two charges in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	medium_permittivity (float): The relative permittivity of the medium in which the charges are present, in F/m. Default is 8.854e-12 (vacuum permittivity).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [charge1,charge2,distance,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_binomial_probability(number_of_trials:int, number_of_successes:int, probability_of_success:float=0.5) -> str:
	"""
	calculate_binomial_probability : Calculates the binomial probability given the number of trials, successes and the probability of success on an individual trial.    
	Parameters:
	number_of_trials (int): The total number of trials.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number_of_successes (int): The desired number of successful outcomes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	probability_of_success (float): The probability of a successful outcome on any given trial.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number_of_trials,number_of_successes,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def find_instrument(budget:int, type:str, make:str=None) -> str:
	"""
	find_instrument : Search for a musical instrument within specified budget and of specific type.    
	Parameters:
	budget (int): Your budget for the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Type of the instrument
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	make (str): Maker of the instrument, Optional parameter. Default to not use it if not provided.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [budget,type,]

	"""
	return 'Success'

tools = [sports_ranking_get_top_player, electromagnetic_force, calculate_binomial_probability, find_instrument]
