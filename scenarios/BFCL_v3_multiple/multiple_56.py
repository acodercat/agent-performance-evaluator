def volume_traded(company, days, data_source=None):
	"""
	Calculate the total volume of stocks traded over a certain period of time    
	Parameters:
	company: Name of the company to get data for
	days: Number of past days to calculate volume traded for
	data_source: Source to fetch the financial data. default is 'yahoo finance'

	"""
	pass

def total_revenue(company, days, data_source=None):
	"""
	Calculate the total revenue of a company over a specific period of time    
	Parameters:
	company: Name of the company to get data for
	days: Number of past days to calculate total revenue for
	data_source: Source to fetch the financial data. default is 'google finance'

	"""
	pass

def avg_closing_price(company, days, data_source=None):
	"""
	Calculate the average closing price of a specific company over a given period of time    
	Parameters:
	company: Name of the company to get data for
	days: Number of past days to calculate average closing price for
	data_source: Source to fetch the stock data. default is 'yahoo finance'

	"""
	pass

tools = [volume_traded, total_revenue, avg_closing_price]
