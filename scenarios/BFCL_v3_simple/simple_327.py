from typing import List, Dict, Any, Union, Tuple, Set 
def sports_team_get_schedule(team_name:str, num_of_games:int, league:str, location:str=None) -> str:
	"""
	sports_team_get_schedule : Fetches the schedule of the specified sports team for the specified number of games in the given league.    
	Parameters:
	team_name (str): The name of the sports team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	num_of_games (int): Number of games for which to fetch the schedule.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): The name of the sports league. If not provided, the function will fetch the schedule for all games, regardless of the league.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Optional. The city or venue where games are to be held. If not provided, default that all venues will be considered.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team_name,num_of_games,league,]

	"""
	return 'Success'

tools = [sports_team_get_schedule]
