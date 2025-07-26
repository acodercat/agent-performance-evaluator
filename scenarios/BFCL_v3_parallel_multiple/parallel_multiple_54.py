from typing import List, Dict, Any, Union, Tuple, Set 
def BattleReignGameAPI_update_player_equipment(attribute:str, level:int, playerID:int=123) -> str:
	"""
	BattleReignGameAPI_update_player_equipment : Modify the player's equipment level for specified attributes    
	Parameters:
	attribute (str): The attribute of the equipment to modify.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	level (int): The level to modify the attribute to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	playerID (int): Player ID of the player. Default to 123
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [attribute,level,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def GameGuideAPI_search_guide(game:str, condition:str='', type:str='') -> str:
	"""
	GameGuideAPI_search_guide : Search for game guides given specific conditions and preferences    
	Parameters:
	game (str): Name of the game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	condition (str): Specific game conditions. (eg: 'snowy weather', 'hard mode').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Specific type of guide. (eg: 'strategy', 'walkthrough')
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game,]

	"""
	return 'Success'

tools = [BattleReignGameAPI_update_player_equipment, GameGuideAPI_search_guide]
