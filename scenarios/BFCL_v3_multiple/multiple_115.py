def find_instrument(budget, type, make=None):
	"""
	Search for a musical instrument within specified budget and of specific type.    
	Parameters:
	budget: Your budget for the instrument.
	type: Type of the instrument
	make: Maker of the instrument, Optional parameter. Default is 'all'

	"""
	pass

def get_stock_info(company_name, detail_level, market=None):
	"""
	Retrieves information about a specific stock based on company's name.    
	Parameters:
	company_name: The name of the company.
	detail_level: Level of detail for stock information. Can be 'summary' or 'detailed'.
	market: The stock market of interest. Default is 'NASDAQ'

	"""
	pass

def find_restaurants(location, food_type, number, dietary_requirements='None'):
	"""
	Locate nearby restaurants based on location and food preferences.    
	Parameters:
	location: The specific location or area.
	food_type: The type of food preferred.
	number: Number of results to return.
	dietary_requirements: Special dietary requirements, e.g. vegan, gluten-free.

	"""
	pass

def sports_match_schedule(team_name, num_matches, league=None):
	"""
	Retrieve the match schedule for a specific sports team.    
	Parameters:
	team_name: The name of the sports team.
	num_matches: The number of upcoming matches you want to get.
	league: The sports league of the team. This is an optional parameter. Default 'all'

	"""
	pass

tools = [find_instrument, get_stock_info, find_restaurants, sports_match_schedule]
