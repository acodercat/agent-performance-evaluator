from typing import List, Dict, Any, Union, Tuple, Set 
def board_game_chess_get_top_players(location:str, minimum_rating:int, number_of_players:int=10) -> str:
	"""
	board_game_chess_get_top_players : Find top chess players in a location based on rating.    
	Parameters:
	location (str): The city you want to find the players from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	minimum_rating (int): Minimum rating to filter the players.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number_of_players (int): Number of players you want to retrieve, default value is 10
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,minimum_rating,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_search_find_closest(location:str, cuisine:str, amenities:List[str]=None) -> str:
	"""
	restaurant_search_find_closest : Locate the closest sushi restaurant based on certain criteria, such as the presence of a patio.    
	Parameters:
	location (str): The city, for instance Boston, MA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cuisine (str): Type of food like Sushi.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amenities (List[str]): Preferred amenities in the restaurant. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,cuisine,]

	"""
	return 'Success'

tools = [board_game_chess_get_top_players, restaurant_search_find_closest]
