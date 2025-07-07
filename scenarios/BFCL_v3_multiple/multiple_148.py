def get_current_time(location, country, timezone=None):
	"""
	Retrieve the current time in a specific time zone.    
	Parameters:
	location: The name of the city.
	country: The name of the country.
	timezone: The optional timezone to get current time. Default ''

	"""
	pass

def get_stock_info(company_name, detail_level, market=None):
	"""
	Retrieves information about a specific stock based on company's name.    
	Parameters:
	company_name: The name of the company.
	detail_level: Level of detail for stock information. Can be 'summary' or 'detailed'.
	market: The stock market of interest. Default is 'NASDAQ'

	"""
	pass

tools = [get_current_time, get_stock_info]
