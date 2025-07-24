from typing import List, Dict, Any, Union, Tuple, Set 
def BoardGameGeek_recommend(numPlayers:int, category:str, difficulty:str=None):
	"""
	BoardGameGeek_recommend : Generate game recommendation from BoardGameGeek store based on number of players and category.    
	Parameters:
	numPlayers (int): The number of players who will play the game.
	category (str): The preferred category of board game. E.g. strategy, family, party etc.
	difficulty (str): Preferred difficulty level. E.g. beginner, intermediate, advanced etc. This is an optional parameter. Default 'beginner'

	Required Parameter = [numPlayers,category,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def AmazonGameStore_recommend(numOfPlayers:int, category:str, priceRange:str=None):
	"""
	AmazonGameStore_recommend : Generate game recommendation from Amazon Game Store based on number of players and category.    
	Parameters:
	numOfPlayers (int): The number of players who will play the game.
	category (str): The preferred category of board game. E.g. strategy, family, party etc.
	priceRange (str): The price range you are willing to pay for the board game. E.g. $10-$20, $20-$30 etc. This is an optional parameter. Default ''

	Required Parameter = [numOfPlayers,category,]

	"""
	return 'Success'

tools = [BoardGameGeek_recommend, AmazonGameStore_recommend]
