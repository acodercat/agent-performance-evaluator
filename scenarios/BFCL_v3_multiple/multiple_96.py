def get_stock_info(company_name, detail_level, market=None):
	"""
	Retrieves information about a specific stock based on company's name.    
	Parameters:
	company_name: The name of the company.
	detail_level: Level of detail for stock information. Can be 'summary' or 'detailed'.
	market: The stock market of interest. Default is 'NASDAQ'

	"""
	pass

def portfolio_future_value(stock, invested_amount, expected_annual_return, years):
	"""
	Calculate the future value of an investment in a specific stock based on the invested amount, expected annual return and number of years.    
	Parameters:
	stock: The ticker symbol of the stock.
	invested_amount: The invested amount in USD.
	expected_annual_return: The expected annual return on investment as a decimal. E.g. 5% = 0.05
	years: The number of years for which the investment is made.

	"""
	pass

def solve_quadratic_equation(a, b, c):
	"""
	Function solves the quadratic equation and returns its roots.    
	Parameters:
	a: Coefficient of x squared
	b: Coefficient of x
	c: Constant term in the quadratic equation

	"""
	pass

tools = [get_stock_info, portfolio_future_value, solve_quadratic_equation]
