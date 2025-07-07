def currency_conversion_convert(from_currency, to_currency, amount):
	"""
	Converts a specified amount of money from one currency to another at the latest rate.    
	Parameters:
	from_currency: The currency that you want to convert from.
	to_currency: The currency that you want to convert to.
	amount: The amount of money that you want to convert.

	"""
	pass

def currency_conversion_get_latest_rate(from_currency, to_currency):
	"""
	Get the latest currency conversion rate from one currency to another.    
	Parameters:
	from_currency: The currency that you want to convert from.
	to_currency: The currency that you want to convert to.

	"""
	pass

def currency_conversion_get_rate(from_currency, to_currency, date='today'):
	"""
	Get the currency conversion rate from one currency to another at a specified date.    
	Parameters:
	from_currency: The currency that you want to convert from.
	to_currency: The currency that you want to convert to.
	date: The date at which the conversion rate applies. Default is the current date.

	"""
	pass

tools = [currency_conversion_convert, currency_conversion_get_latest_rate, currency_conversion_get_rate]
