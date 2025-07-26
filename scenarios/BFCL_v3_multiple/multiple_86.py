from typing import List, Dict, Any, Union, Tuple, Set 
def BoardGameGeek_recommend(numPlayers:int, category:str, difficulty:str=None) -> str:
	"""
	BoardGameGeek_recommend : Generate game recommendation from BoardGameGeek store based on number of players and category.    
	Parameters:
	numPlayers (int): The number of players who will play the game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	category (str): The preferred category of board game. E.g. strategy, family, party etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	difficulty (str): Preferred difficulty level. E.g. beginner, intermediate, advanced etc. This is an optional parameter. Default 'beginner'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [numPlayers,category,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def AmazonGameStore_recommend(numOfPlayers:int, category:str, priceRange:str=None) -> str:
	"""
	AmazonGameStore_recommend : Generate game recommendation from Amazon Game Store based on number of players and category.    
	Parameters:
	numOfPlayers (int): The number of players who will play the game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	category (str): The preferred category of board game. E.g. strategy, family, party etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	priceRange (str): The price range you are willing to pay for the board game. E.g. $10-$20, $20-$30 etc. This is an optional parameter. Default ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [numOfPlayers,category,]

	"""
	return 'Success'

tools = [BoardGameGeek_recommend, AmazonGameStore_recommend]
