def AmazonGameStore_recommend(numOfPlayers, category, priceRange=None):
	"""
	Generate game recommendation from Amazon Game Store based on number of players and category.    
	Parameters:
	numOfPlayers: The number of players who will play the game.
	category: The preferred category of board game. E.g. strategy, family, party etc.
	priceRange: The price range you are willing to pay for the board game. E.g. $10-$20, $20-$30 etc. This is an optional parameter. Default to '$10-$20' if not specified.

	"""
	pass

def BoardGameGeek_recommend(numPlayers, category, difficulty=None):
	"""
	Generate game recommendation from BoardGameGeek store based on number of players and category.    
	Parameters:
	numPlayers: The number of players who will play the game.
	category: The preferred category of board game. E.g. strategy, family, party etc.
	difficulty: Preferred difficulty level. E.g. beginner, intermediate, advanced etc. This is an optional parameter. Default to 'beginner' if not specified.

	"""
	pass

tools = [AmazonGameStore_recommend, BoardGameGeek_recommend]
