def grocery_store_find_nearby(location, categories=None):
	"""
	Locate nearby grocery stores based on specific criteria like organic fruits and vegetables.    
	Parameters:
	location: The city and state, e.g. Houston, TX
	categories: Categories of items to be found in the grocery store. Default is empty array

	"""
	pass

def calculate_NPV(cash_flows, discount_rate, initial_investment=None):
	"""
	Calculate the NPV (Net Present Value) of an investment, considering a series of future cash flows, discount rate, and an initial investment.    
	Parameters:
	cash_flows: Series of future cash flows.
	discount_rate: The discount rate to use.
	initial_investment: The initial investment. Default is 0 if not specified.

	"""
	pass

def get_stock_price(company_name, date, exchange=None):
	"""
	Get the closing stock price for a specific company on a specified date.    
	Parameters:
	company_name: Name of the company.
	date: Date of when to get the stock price. Format: yyyy-mm-dd.
	exchange: Name of the stock exchange market where the company's stock is listed. Default is 'NASDAQ'

	"""
	pass

def instrument_price_get(brand, model, finish):
	"""
	Retrieve the current retail price of a specific musical instrument.    
	Parameters:
	brand: The brand of the instrument.
	model: The specific model of the instrument.
	finish: The color or type of finish on the instrument.

	"""
	pass

tools = [grocery_store_find_nearby, calculate_NPV, get_stock_price, instrument_price_get]
