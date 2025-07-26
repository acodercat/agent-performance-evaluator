from typing import List, Dict, Any, Union, Tuple, Set 
def publication_year_find(author:str, work_title:str, location:str=None) -> str:
	"""
	publication_year_find : Fetches the year a particular scientific work was published.    
	Parameters:
	author (str): Name of the author of the work.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	work_title (str): Title of the scientific work.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Place of the publication, if known. Default is 'global'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [author,work_title,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def portfolio_future_value(stock:str, invested_amount:float, expected_annual_return:float, years:int) -> str:
	"""
	portfolio_future_value : Calculate the future value of an investment in a specific stock based on the invested amount, expected annual return and number of years.    
	Parameters:
	stock (str): The ticker symbol of the stock.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	invested_amount (float): The invested amount in USD.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	expected_annual_return (float): The expected annual return on investment as a decimal. E.g. 5% = 0.05
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	years (int): The number of years for which the investment is made.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [stock,invested_amount,expected_annual_return,years,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def religious_history_get_papal_biography(papal_name:str, include_contributions:bool) -> str:
	"""
	religious_history_get_papal_biography : Retrieve the biography and main religious and historical contributions of a Pope based on his papal name.    
	Parameters:
	papal_name (str): The papal name of the Pope.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_contributions (bool): Include main contributions of the Pope in the response if true.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [papal_name,include_contributions,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def board_game_info(game_name:str, info_required:List[str]) -> str:
	"""
	board_game_info : Get the information about a board game from a database.     
	Parameters:
	game_name (str): Name of the board game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	info_required (List[str]): Array of information requested for the game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game_name,info_required,]

	"""
	return 'Success'

tools = [publication_year_find, portfolio_future_value, religious_history_get_papal_biography, board_game_info]
