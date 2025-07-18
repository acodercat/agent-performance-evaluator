from typing import List, Dict, Any, Union, Tuple 
def get_defense_ranking(season:int, top:int=1):
	"""
	get_defense_ranking : Retrieve the defence ranking of NBA teams in a specified season.    
	Parameters:
	season (int): The NBA season to get defence ranking from.
	top (int): Number of top teams in defence ranking to fetch.

	Required Parameter = [season,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def array_sort(list:List[float], order:str):
	"""
	array_sort : Sorts a given list in ascending or descending order.    
	Parameters:
	list (List[float]): The list of numbers to be sorted.
	order (str): Order of sorting. If not specified, it will default to ascending.

	Required Parameter = [list,order,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def calculate_cagr(initial_value:float, final_value:float, period_in_years:int):
	"""
	calculate_cagr : Calculate the Compound Annual Growth Rate (CAGR) given an initial investment value, a final investment value, and the number of years.    
	Parameters:
	initial_value (float): The initial investment value.
	final_value (float): The final investment value.
	period_in_years (int): The period of the investment in years.

	Required Parameter = [initial_value,final_value,period_in_years,]

	"""
	pass

tools = [get_defense_ranking, array_sort, calculate_cagr]
