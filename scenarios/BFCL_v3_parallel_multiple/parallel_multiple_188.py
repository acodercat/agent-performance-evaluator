from typing import List, Dict, Any, Union, Tuple, Set 
def sports_ranking_get_top_player(sport:str, gender:str='men'):
	"""
	sports_ranking_get_top_player : Get the top player in a specific sport.    
	Parameters:
	sport (str): The type of sport.
	gender (str): The gender of the sport category. Optional.

	Required Parameter = [sport,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def electromagnetic_force(charge1:int, charge2:int, distance:float, medium_permittivity:float=None):
	"""
	electromagnetic_force : Calculate the electromagnetic force between two charges placed at a certain distance.    
	Parameters:
	charge1 (int): The magnitude of the first charge in coulombs.
	charge2 (int): The magnitude of the second charge in coulombs.
	distance (float): The distance between the two charges in meters.
	medium_permittivity (float): The relative permittivity of the medium in which the charges are present, in F/m. Default is 8.854e-12 (vacuum permittivity).

	Required Parameter = [charge1,charge2,distance,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_binomial_probability(number_of_trials:int, number_of_successes:int, probability_of_success:float=0.5):
	"""
	calculate_binomial_probability : Calculates the binomial probability given the number of trials, successes and the probability of success on an individual trial.    
	Parameters:
	number_of_trials (int): The total number of trials.
	number_of_successes (int): The desired number of successful outcomes.
	probability_of_success (float): The probability of a successful outcome on any given trial.

	Required Parameter = [number_of_trials,number_of_successes,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def find_instrument(budget:int, type:str, make:str=None):
	"""
	find_instrument : Search for a musical instrument within specified budget and of specific type.    
	Parameters:
	budget (int): Your budget for the instrument.
	type (str): Type of the instrument
	make (str): Maker of the instrument, Optional parameter. Default to not use it if not provided.

	Required Parameter = [budget,type,]

	"""
	pass

tools = [sports_ranking_get_top_player, electromagnetic_force, calculate_binomial_probability, find_instrument]
