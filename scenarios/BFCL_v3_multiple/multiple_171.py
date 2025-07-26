from typing import List, Dict, Any, Union, Tuple, Set 
def poker_probability_full_house(deck_size:int, hand_size:int) -> str:
	"""
	poker_probability_full_house : Calculate the probability of getting a full house in a poker game.    
	Parameters:
	deck_size (int): The size of the deck. Default is 52.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	hand_size (int): The size of the hand. Default is 5.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [deck_size,hand_size,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def game_result_get_winner(teams:List[str], date:str, venue:str=None) -> str:
	"""
	game_result_get_winner : Get the winner of a specific basketball game.    
	Parameters:
	teams (List[str]): List of two teams who played the game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date of the game, formatted as YYYY-MM-DD.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	venue (str): Optional: The venue of the game. Default is ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [teams,date,]

	"""
	return 'Success'

tools = [poker_probability_full_house, game_result_get_winner]
