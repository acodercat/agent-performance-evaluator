def fetch_DNA_sequence(DNA_id, format=None, upstream=None):
	"""
	Retrieve the sequence of a DNA molecule with the given id from a public database.    
	Parameters:
	DNA_id: Unique ID of the DNA molecule in the database.
	format: Optional parameter to get sequence in specific format (default to 'fasta').
	upstream: Optional parameter to include certain number of base pairs upstream the DNA sequence (default to 0).

	"""
	pass

tools = [fetch_DNA_sequence]
