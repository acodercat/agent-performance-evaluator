from typing import List, Dict, Any, Union, Tuple, Set 
def analyze_structure(building_id:str, floors:List[int], mode:str=None) -> str:
	"""
	analyze_structure : Analyze a structure of a building based on its Id and floor numbers.    
	Parameters:
	building_id (str): The unique identification number of the building.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	floors (List[int]): Floor numbers to be analyzed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mode (str): Mode of analysis, e.g. 'static' or 'dynamic'. Default is 'static'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [building_id,floors,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def player_statistic(player_name:str, year:int, team_name:str=None) -> str:
	"""
	player_statistic : Retrieves detailed player's statistics for a specific year.    
	Parameters:
	player_name (str): The player's name.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year for which the statistics will be displayed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team_name (str): The name of the team(optional). Default is all if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,year,]

	"""
	return 'Success'

tools = [analyze_structure, player_statistic]
