from typing import List, Dict, Any, Union, Tuple, Set 
def identify_color_rgb(color_name:str, standard:str=None) -> str:
	"""
	identify_color_rgb : This function identifies the RGB values of a named color.    
	Parameters:
	color_name (str): Name of the color.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	standard (str): The color standard (e.g. basic, pantone). Default is 'basic'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [color_name,]

	"""
	return 'Success'

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
def guitar_price_find(model:str, condition:str, location:str) -> str:
	"""
	guitar_price_find : Retrieve the price of a specific used guitar model based on its condition and location.    
	Parameters:
	model (str): The model of the guitar.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	condition (str): The condition of the guitar.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location where the guitar is being sold.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [model,condition,location,]

	"""
	return 'Success'

tools = [identify_color_rgb, board_game_chess_get_top_players, guitar_price_find]
