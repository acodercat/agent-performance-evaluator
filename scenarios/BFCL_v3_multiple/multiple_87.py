def games_reviews_find(game, region=None):
	"""
	Find reviews for a specific game.    
	Parameters:
	game: The name of the game.
	region: The region where the reviews are coming from (optional, default is 'global')

	"""
	pass

def games_update_find(game, platform, region=None):
	"""
	Find the latest updates or patches for a specific game on a specified gaming platform.    
	Parameters:
	game: The name of the game.
	platform: The gaming platform, e.g. Xbox, Playstation, PC.
	region: The region of the update (optional, default is 'global')

	"""
	pass

def games_price_find(game, platform):
	"""
	Find the current price for a specific game on a specified gaming platform.    
	Parameters:
	game: The name of the game.
	platform: The gaming platform, e.g. Xbox, Playstation, PC.

	"""
	pass

tools = [games_reviews_find, games_update_find, games_price_find]
