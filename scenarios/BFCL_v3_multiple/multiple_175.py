def find_instrument(budget, type, make=None):
	"""
	Search for a musical instrument within specified budget and of specific type.    
	Parameters:
	budget: Your budget for the instrument.
	type: Type of the instrument
	make: Maker of the instrument, Optional parameter. Default is ''

	"""
	pass

def calculate_binomial_probability(number_of_trials, number_of_successes, probability_of_success=0.5):
	"""
	Calculates the binomial probability given the number of trials, successes and the probability of success on an individual trial.    
	Parameters:
	number_of_trials: The total number of trials.
	number_of_successes: The desired number of successful outcomes.
	probability_of_success: The probability of a successful outcome on any given trial.

	"""
	pass

def electromagnetic_force(charge1, charge2, distance, medium_permittivity=None):
	"""
	Calculate the electromagnetic force between two charges placed at a certain distance.    
	Parameters:
	charge1: The magnitude of the first charge in coulombs.
	charge2: The magnitude of the second charge in coulombs.
	distance: The distance between the two charges in meters.
	medium_permittivity: The relative permittivity of the medium in which the charges are present. Default is 8.854 x 10^-12 F/m (vacuum permittivity).

	"""
	pass

def sports_ranking_get_top_player(sport, gender='men'):
	"""
	Get the top player in a specific sport.    
	Parameters:
	sport: The type of sport.
	gender: The gender of the sport category. Optional.

	"""
	pass

tools = [find_instrument, calculate_binomial_probability, electromagnetic_force, sports_ranking_get_top_player]
