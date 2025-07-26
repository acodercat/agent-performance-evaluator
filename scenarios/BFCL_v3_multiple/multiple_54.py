from typing import List, Dict, Any, Union, Tuple, Set 
def corporate_finance_dividend_data(company:str, years:int, frequency:str=None) -> str:
	"""
	corporate_finance_dividend_data : Get historical dividend data of a specific company within a particular duration.    
	Parameters:
	company (str): The company that you want to get the dividend data for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	years (int): Number of past years for which to retrieve the data.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	frequency (str): The frequency of the dividend payment. Default annually
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,years,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def stock_market_data(company:str, days:int) -> str:
	"""
	stock_market_data : Retrieve stock market data for a specific company and time frame.    
	Parameters:
	company (str): The company that you want to get the stock market data for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of past days for which to retrieve the data.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,days,]

	"""
	return 'Success'

tools = [corporate_finance_dividend_data, stock_market_data]
