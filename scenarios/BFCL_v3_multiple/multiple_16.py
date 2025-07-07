def species_distribution_modeling_project_range_shift(species, climate_scenario, future_time=100):
	"""
	Predict the potential future geographic distribution of a species under a specified climate change scenario.    
	Parameters:
	species: The species of animal.
	climate_scenario: The name of the climate change scenario.
	future_time: The future time in years for the prediction.

	"""
	pass

def population_genetics_calculate_ne(species, generations, probability):
	"""
	Calculate the effective population size necessary to maintain genetic diversity in a wild animal population for a specified number of generations with a given probability.    
	Parameters:
	species: The species of wild animal.
	generations: The number of generations for which to maintain the genetic diversity.
	probability: The probability of maintaining genetic diversity.

	"""
	pass

def ecology_calculate_carrying_capacity(habitat_area, species, productivity):
	"""
	Calculate the maximum population size of the species that the environment can sustain indefinitely.    
	Parameters:
	habitat_area: The area of the habitat in square kilometers.
	species: The species of animal.
	productivity: The biological productivity of the habitat in animals per square kilometer per year.

	"""
	pass

tools = [species_distribution_modeling_project_range_shift, population_genetics_calculate_ne, ecology_calculate_carrying_capacity]
