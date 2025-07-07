def calculate_density(country, year, population, land_area):
	"""
	Calculate the population density of a specific country in a specific year.    
	Parameters:
	country: The country for which the density needs to be calculated.
	year: The year in which the density is to be calculated.
	population: The population of the country.
	land_area: The land area of the country in square kilometers.

	"""
	pass

def crime_record_get_record(case_number, county, details=None):
	"""
	Retrieve detailed felony crime records using a specific case number and location.    
	Parameters:
	case_number: The case number related to the crime.
	county: The county in which the crime occurred.
	details: To get a detailed report, set as true. Defaults to false.

	"""
	pass

def get_highest_scoring_player(game, season, region=None):
	"""
	Retrieve the highest scoring player in a specific game and season.    
	Parameters:
	game: The game in which you want to find the highest scoring player.
	season: The season during which the high score was achieved.
	region: The geographical region in which the game is being played (Optional). Defaults to 'USA'

	"""
	pass

def calculate_compound_interest(principle, interest_rate, time, compounds_per_year=None):
	"""
	Calculates the compound interest of an investment over a given time period.    
	Parameters:
	principle: The initial amount of the investment.
	interest_rate: The yearly interest rate of the investment.
	time: The time, in years, the money is invested or borrowed for.
	compounds_per_year: The number of times the interest is compounded per year. Default is 1 (interest is compounded yearly).

	"""
	pass

tools = [calculate_density, crime_record_get_record, get_highest_scoring_player, calculate_compound_interest]
