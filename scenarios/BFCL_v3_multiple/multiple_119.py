from typing import List, Dict, Any, Union, Tuple, Set 
def average_batting_score(player_name:str, matches:int, match_format:str=None) -> str:
	"""
	average_batting_score : Get the average batting score of a cricketer for specified past matches.    
	Parameters:
	player_name (str): Name of the cricket player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	matches (int): Number of past matches to consider for average calculation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	match_format (str): Format of the cricket matches considered (e.g., 'T20', 'ODI', 'Test'). Default is 'T20'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,matches,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_return_on_investment(purchase_price:float, sale_price:float, dividend:float=0) -> str:
	"""
	calculate_return_on_investment : Calculate the return on investment for a given stock based on its purchase price, sale price, and any dividends received.    
	Parameters:
	purchase_price (float): The price the stock was bought at.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	sale_price (float): The price the stock was sold at.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dividend (float): Any dividends received from the stock.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [purchase_price,sale_price,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def database_query(table:str, conditions:List[Dict[str, str]]) -> str:
	"""
	database_query : Query the database based on certain conditions.    
	Parameters:
	table (str): Name of the table to query.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	conditions (List[Dict[str, str]]): Conditions for the query.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [table,conditions,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def probability_of_event(success_outcomes:int, total_outcomes:int, format_as_ratio:bool=None) -> str:
	"""
	probability_of_event : Calculates the probability of an event.    
	Parameters:
	success_outcomes (int): The number of successful outcomes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	total_outcomes (int): The total number of possible outcomes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	format_as_ratio (bool): When true, formats the output as a ratio instead of a decimal. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [success_outcomes,total_outcomes,]

	"""
	return 'Success'

tools = [average_batting_score, calculate_return_on_investment, database_query, probability_of_event]
