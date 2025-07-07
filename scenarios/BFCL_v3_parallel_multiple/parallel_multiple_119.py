def team_stats_get_top_scorer(team_name, competition=None):
	"""
	Fetch the top scorer of a specified football team.    
	Parameters:
	team_name: The name of the football team.
	competition: Competition for which to fetch stats (optional). Default is 'Premier League' if not specified.

	"""
	pass

def league_stats_get_top_scorer(league_name, season=None):
	"""
	Fetch the top scorer of a specified football league.    
	Parameters:
	league_name: The name of the football league.
	season: Season for which to fetch stats (optional). Default is '2019-2020' if not specified.

	"""
	pass

def player_stats_get_all_time_goals(player_name, team_name, competition=None):
	"""
	Fetch all-time goals scored by a particular football player for a specified team.    
	Parameters:
	player_name: The name of the football player.
	team_name: The name of the team for which player has played.
	competition: Competition for which to fetch stats (optional). Default is 'Premier League' if not specified.

	"""
	pass

tools = [team_stats_get_top_scorer, league_stats_get_top_scorer, player_stats_get_all_time_goals]
