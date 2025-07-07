def park_information(park_name, information):
	"""
	Retrieve the basic information such as elevation and area of a national park.    
	Parameters:
	park_name: The name of the national park.
	information: The type of information you want about the park.

	"""
	pass

def legal_case_fetch(case_id, details):
	"""
	Fetch detailed legal case information from database.    
	Parameters:
	case_id: The ID of the legal case.
	details: True if need the detail info. Default is false.

	"""
	pass

def calculate_stock_return(investment_amount, annual_growth_rate, holding_period, include_dividends=None):
	"""
	Calculate the projected return of a stock investment given the investment amount, the annual growth rate and holding period in years.    
	Parameters:
	investment_amount: The amount of money to invest.
	annual_growth_rate: The expected annual growth rate of the stock.
	holding_period: The number of years you intend to hold the stock.
	include_dividends: Optional. True if the calculation should take into account potential dividends. Default is false.

	"""
	pass

tools = [park_information, legal_case_fetch, calculate_stock_return]
