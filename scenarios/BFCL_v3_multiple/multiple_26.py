def game_scores_get(game, platform, level, player=None):
	"""
	Retrieve scores and rankings based on player’s performance in a certain game.    
	Parameters:
	game: The name of the game.
	platform: The gaming platform e.g. Xbox, Playstation, PC
	level: The level of the game for which you want to retrieve the scores.
	player: The name of the player for whom you want to retrieve scores. Default ''

	"""
	pass

def game_rewards_get(game, platform, mission=None, trophy=None):
	"""
	Retrieve information about different types of rewards that you can receive when playing a certain game.    
	Parameters:
	game: The name of the game.
	platform: The gaming platform e.g. Xbox, Playstation, PC
	mission: The mission for which you want to know the rewards. Default to ''
	trophy: The trophy level for which you want to know the rewards. Default to ''

	"""
	pass

def game_missions_list(game):
	"""
	List all missions for a certain game.    
	Parameters:
	game: The name of the game.

	"""
	pass

tools = [game_scores_get, game_rewards_get, game_missions_list]
