from typing import List, Dict, Any, Union, Tuple, Set 
def get_stock_data(symbol:str, data_points:List[str]) -> str:
	"""
	get_stock_data : Retrieve the most recent trading day's closing price and volume for a specified stock.    
	Parameters:
	symbol (str): The stock symbol of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	data_points (List[str]): The type of data you want to retrieve for the stock. This can include closing price, opening price, volume, etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [symbol,data_points,]

	"""
	return 'Success'

tools = [get_stock_data]
