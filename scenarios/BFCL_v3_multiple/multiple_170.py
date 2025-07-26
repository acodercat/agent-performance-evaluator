from typing import List, Dict, Any, Union, Tuple, Set 
def park_information(park_name:str, information:List[str]) -> str:
	"""
	park_information : Retrieve the basic information such as elevation and area of a national park.    
	Parameters:
	park_name (str): The name of the national park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	information (List[str]): The type of information you want about the park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [park_name,information,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def us_history_get_president(event:str, year:int) -> str:
	"""
	us_history_get_president : Retrieve the U.S. president during a specific event in American history.    
	Parameters:
	event (str): The event in U.S. history.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The specific year of the event.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [event,year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def monopoly_odds_calculator(number:int, dice_number:int, dice_faces:int=None) -> str:
	"""
	monopoly_odds_calculator : Calculates the probability of rolling a certain sum with two dice, commonly used in board game like Monopoly.    
	Parameters:
	number (int): The number for which the odds are calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dice_number (int): The number of dice involved in the roll.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dice_faces (int): The number of faces on a single die. Default is 6 for standard six-faced die.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number,dice_number,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def soccer_stat_get_player_stats(player_name:str, season:str, league:str=None) -> str:
	"""
	soccer_stat_get_player_stats : Retrieve soccer player statistics for a given season.    
	Parameters:
	player_name (str): Name of the player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): Soccer season, usually specified by two years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): Optional - the soccer league, defaults to all leagues. Default 'all'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,season,]

	"""
	return 'Success'

tools = [park_information, us_history_get_president, monopoly_odds_calculator, soccer_stat_get_player_stats]
