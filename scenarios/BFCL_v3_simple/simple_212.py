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

tools = [get_stock_info]
