from typing import List, Dict, Any, Union, Tuple 
def card_game_search(theme:str):
	"""
	card_game_search : Locate a card game based on a specific theme.    
	Parameters:
	theme (str): The theme for the card game.

	Required Parameter = [theme,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def board_game_search(complexity:float, player_count:int):
	"""
	board_game_search : Locate a board game based on specific criteria.    
	Parameters:
	complexity (float): The maximum complexity rating of the board game (lower is simpler).
	player_count (int): The minimum player count for the board game.

	Required Parameter = [complexity,player_count,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def trivia_game_search(duration:float):
	"""
	trivia_game_search : Locate a trivia game based on play duration.    
	Parameters:
	duration (float): The maximum playing duration for the trivia game in minutes.

	Required Parameter = [duration,]

	"""
	pass

tools = [card_game_search, board_game_search, trivia_game_search]
