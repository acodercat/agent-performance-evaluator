from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_find_nearby(location:str, dietary_preference:List[str]=None) -> str:
	"""
	restaurant_find_nearby : Locate nearby restaurants based on specific dietary preferences.    
	Parameters:
	location (str): The city and state, e.g. Los Angeles, CA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dietary_preference (List[str]): Dietary preference. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def market_performance_get_data(indexes:List[str], days:int, detailed:bool=None) -> str:
	"""
	market_performance_get_data : Retrieve the market performance data for specified indexes over a specified time period.    
	Parameters:
	indexes (List[str]): Array of stock market indexes. Supported indexes are 'S&P 500', 'Dow Jones', 'NASDAQ', 'FTSE 100', 'DAX' etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of days in the past for which the performance data is required.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detailed (bool): Whether to return detailed performance data. If set to true, returns high, low, opening, and closing prices. If false, returns only closing prices. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [indexes,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sports_match_results(team1:str, team2:str, season:str=None) -> str:
	"""
	sports_match_results : Returns the results of a given match between two teams.    
	Parameters:
	team1 (str): The name of the first team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team2 (str): The name of the second team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): The season when the match happened. Default is the current season.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team1,team2,]

	"""
	return 'Success'

tools = [restaurant_find_nearby, market_performance_get_data, sports_match_results]
