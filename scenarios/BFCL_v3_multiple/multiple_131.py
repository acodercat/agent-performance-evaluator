def restaurant_find_nearby(location, dietary_preference=None):
	"""
	Locate nearby restaurants based on specific dietary preferences.    
	Parameters:
	location: The city and state, e.g. Los Angeles, CA
	dietary_preference: Dietary preference. Default is empty array.

	"""
	pass

def market_performance_get_data(indexes, days, detailed=None):
	"""
	Retrieve the market performance data for specified indexes over a specified time period.    
	Parameters:
	indexes: Array of stock market indexes. Supported indexes are 'S&P 500', 'Dow Jones', 'NASDAQ', 'FTSE 100', 'DAX' etc.
	days: Number of days in the past for which the performance data is required.
	detailed: Whether to return detailed performance data. If set to true, returns high, low, opening, and closing prices. If false, returns only closing prices. Default is false.

	"""
	pass

def sports_match_results(team1, team2, season=None):
	"""
	Returns the results of a given match between two teams.    
	Parameters:
	team1: The name of the first team.
	team2: The name of the second team.
	season: The season when the match happened. Default is the current season.

	"""
	pass

tools = [restaurant_find_nearby, market_performance_get_data, sports_match_results]
