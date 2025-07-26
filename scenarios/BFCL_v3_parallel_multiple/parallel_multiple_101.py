from typing import List, Dict, Any, Union, Tuple, Set 
def volume_traded(company:str, days:int, data_source:str=None) -> str:
	"""
	volume_traded : Calculate the total volume of stocks traded over a certain period of time    
	Parameters:
	company (str): Name of the company to get data for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of past days to calculate volume traded for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	data_source (str): Source to fetch the financial data. default is 'yahoo finance'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def total_revenue(company:str, days:int, data_source:str=None) -> str:
	"""
	total_revenue : Calculate the total revenue of a company over a specific period of time    
	Parameters:
	company (str): Name of the company to get data for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of past days to calculate total revenue for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	data_source (str): Source to fetch the financial data. default is 'google finance'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def avg_closing_price(company:str, days:int, data_source:str=None) -> str:
	"""
	avg_closing_price : Calculate the average closing price of a specific company over a given period of time    
	Parameters:
	company (str): Name of the company to get data for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of past days to calculate average closing price for
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	data_source (str): Source to fetch the stock data. default is 'yahoo finance'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,days,]

	"""
	return 'Success'

tools = [volume_traded, total_revenue, avg_closing_price]
