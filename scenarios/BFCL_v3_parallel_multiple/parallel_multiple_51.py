from typing import List, Dict, Any, Union, Tuple, Set 
def get_team_info(team:str, info:str) -> str:
	"""
	get_team_info : Retrieve information for a specific team, such as championships won.    
	Parameters:
	team (str): The name of the team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	info (str): The information sought. E.g., 'championships_won'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team,info,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_player_record(player:str, stat:str) -> str:
	"""
	get_player_record : Retrieve record stats for a specific player and stat type.    
	Parameters:
	player (str): The name of the player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	stat (str): The type of statistic. E.g., 'highest_scoring_game', 'total_championships'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player,stat,]

	"""
	return 'Success'

tools = [get_team_info, get_player_record]
