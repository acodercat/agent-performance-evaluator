def cellbio_get_proteins(cell_compartment, include_description=False):
	"""
	Get the list of proteins in a specific cell compartment.    
	Parameters:
	cell_compartment: The specific cell compartment.
	include_description: Set true if you want a brief description of each protein.

	"""
	pass

def mutation_type_find(snp_id, species=None):
	"""
	Finds the type of a genetic mutation based on its SNP (Single Nucleotide Polymorphism) ID.    
	Parameters:
	snp_id: The ID of the Single Nucleotide Polymorphism (SNP) mutation.
	species: Species in which the SNP occurs, default is 'Homo sapiens' (Humans).

	"""
	pass

def find_exhibition(location, art_form, month, user_ratings=None):
	"""
	Locate the most popular exhibitions based on criteria like location, time, art form, and user ratings.    
	Parameters:
	location: The city where the exhibition is held, e.g., New York, NY.
	art_form: The form of art the exhibition is displaying e.g., sculpture.
	month: The month (in full name) of exhibition.
	user_ratings: Select exhibitions with user rating threshold. Default is all if not specified.

	"""
	pass

tools = [cellbio_get_proteins, mutation_type_find, find_exhibition]
