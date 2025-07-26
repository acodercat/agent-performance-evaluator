from typing import List, Dict, Any, Union, Tuple, Set 
def find_instrument(budget:float, type:str, make:str=None) -> str:
	"""
	find_instrument : Search for a musical instrument within specified budget and of specific type.    
	Parameters:
	budget (float): Your budget for the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Type of the instrument
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	make (str): Maker of the instrument, Optional parameter. Default is 'all'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [budget,type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_stock_info(company_name:str, detail_level:str, market:str=None) -> str:
	"""
	get_stock_info : Retrieves information about a specific stock based on company's name.    
	Parameters:
	company_name (str): The name of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detail_level (str): Level of detail for stock information. Can be 'summary' or 'detailed'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	market (str): The stock market of interest. Default is 'NASDAQ'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,detail_level,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def find_restaurants(location:str, food_type:str, number:int, dietary_requirements:List[str]='None') -> str:
	"""
	find_restaurants : Locate nearby restaurants based on location and food preferences.    
	Parameters:
	location (str): The specific location or area.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	food_type (str): The type of food preferred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number (int): Number of results to return.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dietary_requirements (List[str]): Special dietary requirements, e.g. vegan, gluten-free.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,food_type,number,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sports_match_schedule(team_name:str, num_matches:int, league:str=None) -> str:
	"""
	sports_match_schedule : Retrieve the match schedule for a specific sports team.    
	Parameters:
	team_name (str): The name of the sports team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	num_matches (int): The number of upcoming matches you want to get.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): The sports league of the team. This is an optional parameter. Default 'all'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team_name,num_matches,]

	"""
	return 'Success'

tools = [find_instrument, get_stock_info, find_restaurants, sports_match_schedule]
