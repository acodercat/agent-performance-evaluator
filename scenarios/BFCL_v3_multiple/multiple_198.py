def calculate_genotype_frequency(allele_frequency, genotype):
	"""
	Calculate the frequency of homozygous dominant genotype based on the allele frequency using Hardy Weinberg Principle.    
	Parameters:
	allele_frequency: The frequency of the dominant allele in the population.
	genotype: The genotype which frequency is needed, default is homozygous dominant. 

	"""
	pass

def hotel_booking(hotel_name, location, start_date, end_date, rooms=1):
	"""
	Books a hotel room for a specific date range.    
	Parameters:
	hotel_name: The name of the hotel.
	location: The city and state, e.g. New York, NY.
	start_date: The start date of the reservation. Use format 'YYYY-MM-DD'.
	end_date: The end date of the reservation. Use format 'YYYY-MM-DD'.
	rooms: The number of rooms to reserve.

	"""
	pass

def get_highest_scoring_player(game, season, region=None):
	"""
	Retrieve the highest scoring player in a specific game and season.    
	Parameters:
	game: The game in which you want to find the highest scoring player.
	season: The season during which the high score was achieved.
	region: The geographical region in which the game is being played (Optional). Default is 'all'

	"""
	pass

def science_history_get_invention(invention_name, want_year):
	"""
	Retrieve the inventor and year of invention based on the invention's name.    
	Parameters:
	invention_name: The name of the invention.
	want_year: Return the year of invention if set to true.

	"""
	pass

tools = [calculate_genotype_frequency, hotel_booking, get_highest_scoring_player, science_history_get_invention]
