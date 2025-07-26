from typing import List, Dict, Any, Union, Tuple, Set 
def sports_ranking_get_current(team:str, league:str, season:str=None) -> str:
	"""
	sports_ranking_get_current : Retrieve the current ranking of a specific team in a particular league.    
	Parameters:
	team (str): The name of the team whose ranking is sought.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): The league in which the team participates.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): The season for which the ranking is sought. Defaults to the current season '2023-2024' if not provided.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team,league,]

	"""
	return 'Success'

tools = [sports_ranking_get_current]
