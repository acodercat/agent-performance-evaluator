from typing import List, Dict, Any, Union, Tuple 
def get_current_time(location:str, country:str, timezone:str=None):
	"""
	get_current_time : Retrieve the current time in a specific time zone.    
	Parameters:
	location (str): The name of the city.
	country (str): The name of the country.
	timezone (str): The optional timezone to get current time. Default ''

	Required Parameter = [location,country,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def get_stock_info(company_name:str, detail_level:str, market:str=None):
	"""
	get_stock_info : Retrieves information about a specific stock based on company's name.    
	Parameters:
	company_name (str): The name of the company.
	detail_level (str): Level of detail for stock information. Can be 'summary' or 'detailed'.
	market (str): The stock market of interest. Default is 'NASDAQ'

	Required Parameter = [company_name,detail_level,]

	"""
	pass

tools = [get_current_time, get_stock_info]
