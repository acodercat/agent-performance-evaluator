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

tools = [market_performance_get_data]
