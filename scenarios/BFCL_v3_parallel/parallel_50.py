from typing import List, Dict, Any, Union, Tuple, Set 
def game_save_progress(stage:int, mode:str, level:str='user') -> str:
	"""
	game_save_progress : Save the current state of a player's game, given the stage, level and game mode.    
	Parameters:
	stage (int): The current stage in the game the player has reached.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mode (str): The game mode. Available modes are easy or hard.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	level (str): The player's level.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [stage,mode,]

	"""
	return 'Success'

tools = [game_save_progress]
