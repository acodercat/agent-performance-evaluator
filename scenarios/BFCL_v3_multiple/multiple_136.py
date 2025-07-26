from typing import List, Dict, Any, Union, Tuple, Set 
def get_crime_rate(city:str, state:str, type:str=None, year:int=None) -> str:
	"""
	get_crime_rate : Retrieve the official crime rate of a city.    
	Parameters:
	city (str): The name of the city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	state (str): The state where the city is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Optional. The type of crime. Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Optional. The year for the crime rate data. Defaults to 2024.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city,state,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def poker_game_winner(players:List[str], cards:Dict[str, Any], type:str=None) -> str:
	"""
	poker_game_winner : Identify the winner in a poker game based on the cards.    
	Parameters:
	players (List[str]): Names of the players in a list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cards (Dict[str, Any]): An object containing the player name as key and the cards as values in a list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Type of poker game. Defaults to 'Texas Holdem'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [players,cards,]

	"""
	return 'Success'

tools = [get_crime_rate, poker_game_winner]
