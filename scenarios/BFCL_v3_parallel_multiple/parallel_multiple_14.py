def crop_yield_get_history(country, crop, years):
	"""
	Retrieve historical crop yield data of a specific crop in a given country.    
	Parameters:
	country: The country of interest.
	crop: Type of crop.
	years: Number of years of history to retrieve.

	"""
	pass

def animal_population_get_history(country, species, years):
	"""
	Retrieve historical population size of a specific species in a given country.    
	Parameters:
	country: The country of interest.
	species: Species of the animal.
	years: Number of years of history to retrieve.

	"""
	pass

def animal_population_get_projection(country, species, years):
	"""
	Predict the future population size of a specific species in a given country.    
	Parameters:
	country: The country of interest.
	species: Species of the animal.
	years: Number of years in the future to predict.

	"""
	pass

tools = [crop_yield_get_history, animal_population_get_history, animal_population_get_projection]
