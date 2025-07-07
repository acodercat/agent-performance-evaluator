def basketball_player_stats_get(player_name, stats_fields):
	"""
	Get current statistics for a specified basketball player    
	Parameters:
	player_name: The name of the player.
	stats_fields: List of statistical categories to be fetched, including points, assists, rebounds, minutes.

	"""
	pass

def basketball_game_stats_get(team1, team2, date, stats_fields=None):
	"""
	Get the detailed statistical data from a specific basketball game    
	Parameters:
	team1: One of the competing teams in the game.
	team2: One of the competing teams in the game.
	date: The date when the game occurred.
	stats_fields: List of statistical categories to be fetched, including total points, total assists, total rebounds, turnovers. Default to empty list

	"""
	pass

def basketball_team_stats_get(team_name, stats_fields):
	"""
	Get current statistics for a specific basketball team    
	Parameters:
	team_name: The name of the team.
	stats_fields: List of statistical categories to be fetched, including total points, total assists, total rebounds, win rate.

	"""
	pass

tools = [basketball_player_stats_get, basketball_game_stats_get, basketball_team_stats_get]
