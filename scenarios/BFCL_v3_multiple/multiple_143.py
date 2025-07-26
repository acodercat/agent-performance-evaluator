from typing import List, Dict, Any, Union, Tuple, Set 
def create_player_profile(player_name:str, _class:str, starting_level:int=1) -> str:
	"""
	create_player_profile : Create a new player profile with character name, class and starting level.    
	Parameters:
	player_name (str): The desired name of the player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	_class (str): The character class for the player
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	starting_level (int): The starting level for the player
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,_class,]

	"""
	return 'Success'

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
def concert_find_nearby(location:str, genre:str) -> str:
	"""
	concert_find_nearby : Locate nearby concerts based on specific criteria like genre.    
	Parameters:
	location (str): The city and state, e.g. Seattle, WA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	genre (str): Genre of music to be played at the concert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,genre,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_slope_gradient(point1:List[float], point2:List[float], unit:str=None) -> str:
	"""
	calculate_slope_gradient : Calculate the slope gradient between two geographical coordinates.    
	Parameters:
	point1 (List[float]): The geographic coordinates for the first point [Latitude, Longitude].
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	point2 (List[float]): The geographic coordinates for the second point [Latitude, Longitude].
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The unit for the slope gradient. Default is 'degree'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [point1,point2,]

	"""
	return 'Success'

tools = [create_player_profile, poker_probability_full_house, concert_find_nearby, calculate_slope_gradient]
