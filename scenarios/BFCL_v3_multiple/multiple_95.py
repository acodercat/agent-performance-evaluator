def currency_exchange_convert(amount, from_currency, to_currency, live_conversion=None):
	"""
	Converts a value from one currency to another using the latest exchange rate.    
	Parameters:
	amount: The amount of money to be converted.
	from_currency: The currency to convert from.
	to_currency: The currency to convert to.
	live_conversion: If true, use the latest exchange rate for conversion, else use the last known rate. Default false

	"""
	pass

def unit_conversion_convert(value, from_unit, to_unit):
	"""
	Converts a value from one unit to another.    
	Parameters:
	value: The value to be converted.
	from_unit: The unit to convert from.
	to_unit: The unit to convert to.

	"""
	pass

tools = [currency_exchange_convert, unit_conversion_convert]
