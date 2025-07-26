from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_cagr(initial_value:int, final_value:int, period_in_years:int) -> str:
	"""
	calculate_cagr : Calculate the Compound Annual Growth Rate (CAGR) given an initial investment value, a final investment value, and the number of years.    
	Parameters:
	initial_value (int): The initial investment value.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	final_value (int): The final investment value.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	period_in_years (int): The period of the investment in years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [initial_value,final_value,period_in_years,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def chess_rating(player_name:str, variant:str=None) -> str:
	"""
	chess_rating : Fetches the current chess rating of a given player    
	Parameters:
	player_name (str): The full name of the chess player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	variant (str): The variant of chess for which rating is requested (e.g., 'classical', 'blitz', 'bullet'). Default is 'classical'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [player_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def solve_quadratic(a:int, b:int, c:int) -> str:
	"""
	solve_quadratic : Find the roots of a quadratic equation. Returns both roots.    
	Parameters:
	a (int): Coefficient of x².
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	b (int): Coefficient of x.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	c (int): Constant term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [a,b,c,]

	"""
	return 'Success'

tools = [calculate_cagr, chess_rating, solve_quadratic]
