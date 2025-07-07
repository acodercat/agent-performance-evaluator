def park_information(park_name, information):
	"""
	Retrieve the basic information such as elevation and area of a national park.    
	Parameters:
	park_name: The name of the national park.
	information: The type of information you want about the park.

	"""
	pass

def us_history_get_president(event, year):
	"""
	Retrieve the U.S. president during a specific event in American history.    
	Parameters:
	event: The event in U.S. history.
	year: The specific year of the event.

	"""
	pass

def monopoly_odds_calculator(number, dice_number, dice_faces=None):
	"""
	Calculates the probability of rolling a certain sum with two dice, commonly used in board game like Monopoly.    
	Parameters:
	number: The number for which the odds are calculated.
	dice_number: The number of dice involved in the roll.
	dice_faces: The number of faces on a single die. Default is 6 for standard six-faced die.

	"""
	pass

def soccer_stat_get_player_stats(player_name, season, league=None):
	"""
	Retrieve soccer player statistics for a given season.    
	Parameters:
	player_name: Name of the player.
	season: Soccer season, usually specified by two years.
	league: Optional - the soccer league, defaults to all leagues. Default 'all'

	"""
	pass

tools = [park_information, us_history_get_president, monopoly_odds_calculator, soccer_stat_get_player_stats]
