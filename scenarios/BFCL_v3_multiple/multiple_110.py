def get_collectables_in_season(game_name, season, item_type=None):
	"""
	Retrieve a list of collectable items in a specific game during a specified season.    
	Parameters:
	game_name: Name of the game.
	season: The season for which to retrieve the collectable items.
	item_type: The type of item to search for. Default is 'all'. Possible values: 'all', 'bug', 'fish', 'sea creatures', etc.

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

tools = [get_collectables_in_season, mutation_type_find]
