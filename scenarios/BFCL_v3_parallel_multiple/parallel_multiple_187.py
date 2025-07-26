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
def get_defense_ranking(season:int, top:int=1) -> str:
	"""
	get_defense_ranking : Retrieve the defence ranking of NBA teams in a specified season.    
	Parameters:
	season (int): The NBA season to get defence ranking from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	top (int): Number of top teams in defence ranking to fetch.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [season,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def array_sort(list:List[float], order:str) -> str:
	"""
	array_sort : Sorts a given list in ascending or descending order.    
	Parameters:
	list (List[float]): The list of numbers to be sorted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	order (str): Order of sorting. If not specified, it will default to ascending.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [list,order,]

	"""
	return 'Success'

tools = [calculate_cagr, get_defense_ranking, array_sort]
