from typing import List, Dict, Any, Union, Tuple 
def team_stats_get_top_scorer(team_name:str, competition:str=None):
	"""
	team_stats_get_top_scorer : Fetch the top scorer of a specified football team.    
	Parameters:
	team_name (str): The name of the football team.
	competition (str): Competition for which to fetch stats (optional). Default is 'Premier League' if not specified.

	Required Parameter = [team_name,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def league_stats_get_top_scorer(league_name:str, season:str=None):
	"""
	league_stats_get_top_scorer : Fetch the top scorer of a specified football league.    
	Parameters:
	league_name (str): The name of the football league.
	season (str): Season for which to fetch stats (optional). Default is '2019-2020' if not specified.

	Required Parameter = [league_name,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def player_stats_get_all_time_goals(player_name:str, team_name:str, competition:str=None):
	"""
	player_stats_get_all_time_goals : Fetch all-time goals scored by a particular football player for a specified team.    
	Parameters:
	player_name (str): The name of the football player.
	team_name (str): The name of the team for which player has played.
	competition (str): Competition for which to fetch stats (optional). Default is 'Premier League' if not specified.

	Required Parameter = [player_name,team_name,]

	"""
	pass

tools = [team_stats_get_top_scorer, league_stats_get_top_scorer, player_stats_get_all_time_goals]
