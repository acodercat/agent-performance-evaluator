def math_power(base, exponent, mod=None):
	"""
	Calculate the power of one number raised to another.    
	Parameters:
	base: The base number.
	exponent: The exponent.
	mod: The modulus. Default is None. Calculates pow(base, exponent) % mod when provided.

	"""
	pass

def probabilities_calculate_single(total_outcomes, event_outcomes, round=None):
	"""
	Calculate the probability of an event.    
	Parameters:
	total_outcomes: The total number of outcomes.
	event_outcomes: The number of outcomes where the event occurs.
	round: Round the answer to a specified number of decimal places. Defaults to 2.

	"""
	pass

def fetch_DNA_sequence(DNA_id, format=None, upstream=None):
	"""
	Retrieve the sequence of a DNA molecule with the given id from a public database.    
	Parameters:
	DNA_id: Unique ID of the DNA molecule in the database.
	format: Optional parameter to get sequence in specific format (default to 'fasta').
	upstream: Optional parameter to include certain number of base pairs upstream the DNA sequence (default to 0).

	"""
	pass

tools = [math_power, probabilities_calculate_single, fetch_DNA_sequence]
