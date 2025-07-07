def BattleReignGameAPI_update_player_equipment(attribute, level, playerID=123):
	"""
	Modify the player's equipment level for specified attributes    
	Parameters:
	attribute: The attribute of the equipment to modify.
	level: The level to modify the attribute to.
	playerID: Player ID of the player. Default to 123

	"""
	pass

def GameGuideAPI_search_guide(game, condition='', type=''):
	"""
	Search for game guides given specific conditions and preferences    
	Parameters:
	game: Name of the game.
	condition: Specific game conditions. (eg: 'snowy weather', 'hard mode').
	type: Specific type of guide. (eg: 'strategy', 'walkthrough')

	"""
	pass

tools = [BattleReignGameAPI_update_player_equipment, GameGuideAPI_search_guide]
