from typing import List, Dict, Any, Union, Tuple, Set 
def video_games_store_currency(platform:str, region:str='True') -> str:
	"""
	video_games_store_currency : Fetches the currency used in a specific region in a gaming platform store.    
	Parameters:
	platform (str): The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): The region e.g. United States, United Kingdom, Japan
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [platform,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def video_games_on_sale(game_title:str, platform:str, region:str=None) -> str:
	"""
	video_games_on_sale : Checks if a particular game is currently on sale in a specific gaming platform store and in a specific region.    
	Parameters:
	game_title (str): The title of the video game
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	platform (str): The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): The region e.g. United States, United Kingdom, Japan. Default United States
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game_title,platform,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def video_games_store_price(game_title:str, platform:str, region:str=None) -> str:
	"""
	video_games_store_price : Fetches the selling price of a specified game in a particular gaming platform store and in a specific region.    
	Parameters:
	game_title (str): The title of the video game
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	platform (str): The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): The region e.g. United States, United Kingdom, Japan. Default to United States
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game_title,platform,]

	"""
	return 'Success'

tools = [video_games_store_currency, video_games_on_sale, video_games_store_price]
