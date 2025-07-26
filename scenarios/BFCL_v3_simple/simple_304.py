from typing import List, Dict, Any, Union, Tuple, Set 
def player_stats_getLastGame(player_name:str, team:str, metrics:List[str]=None) -> str:
	"""
	player_stats_getLastGame : Get last game statistics for a specific player in basketball    
	Parameters:
	player_name (str): The name of the basketball player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team (str): The team that player currently plays for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	metrics (List[str]): Specific metrics to retrieve. If no value is specified, all available metrics will be returned by default.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,team,]

	"""
	return 'Success'

tools = [player_stats_getLastGame]
