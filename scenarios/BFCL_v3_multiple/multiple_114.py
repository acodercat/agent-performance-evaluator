def modify_painting(size, medium, dominant_color=None):
	"""
	Modify an existing painting's attributes such as size, medium, and color.    
	Parameters:
	size: The size of the painting in inches, width by height.
	medium: The medium of the painting, such as oil, acrylic, etc.
	dominant_color: The dominant color of the painting. Default ''

	"""
	pass

def prediction_evolution(species, years, model=None):
	"""
	Predict the evolutionary rate for a specific species for a given timeframe.    
	Parameters:
	species: The species that the evolution rate will be predicted for.
	years: Number of years for the prediction.
	model: The model used to make the prediction, options: 'Darwin', 'Lamarck', default is 'Darwin'.

	"""
	pass

def calculate_probability(total_outcomes, favorable_outcomes, round_to=2):
	"""
	Calculate the probability of an event.    
	Parameters:
	total_outcomes: Total number of possible outcomes.
	favorable_outcomes: Number of outcomes considered as 'successful'.
	round_to: Number of decimal places to round the result to.

	"""
	pass

tools = [modify_painting, prediction_evolution, calculate_probability]
