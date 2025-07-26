from typing import List, Dict, Any, Union, Tuple, Set 
def team_stats_get_top_scorer(team_name:str, competition:str=None) -> str:
	"""
	team_stats_get_top_scorer : Fetch the top scorer of a specified football team.    
	Parameters:
	team_name (str): The name of the football team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	competition (str): Competition for which to fetch stats (optional). Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def league_stats_get_top_scorer(league_name:str, season:str=None) -> str:
	"""
	league_stats_get_top_scorer : Fetch the top scorer of a specified football league.    
	Parameters:
	league_name (str): The name of the football league.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): Season for which to fetch stats (optional). Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [league_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def player_stats_get_all_time_goals(player_name:str, team_name:str, competition:str=None) -> str:
	"""
	player_stats_get_all_time_goals : Fetch all-time goals scored by a particular football player for a specified team.    
	Parameters:
	player_name (str): The name of the football player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team_name (str): The name of the team for which player has played.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	competition (str): Competition for which to fetch stats (optional). Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,team_name,]

	"""
	return 'Success'

tools = [team_stats_get_top_scorer, league_stats_get_top_scorer, player_stats_get_all_time_goals]
