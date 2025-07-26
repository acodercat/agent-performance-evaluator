from typing import List, Dict, Any, Union, Tuple, Set 
def unit_conversion_convert(value:int, from_unit:str, to_unit:str) -> str:
	"""
	unit_conversion_convert : Converts a value from one unit to another.    
	Parameters:
	value (int): The value to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_unit (str): The unit to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_unit (str): The unit to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [value,from_unit,to_unit,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def currency_exchange_convert(amount:int, from_currency:str, to_currency:str, live_conversion:bool=None) -> str:
	"""
	currency_exchange_convert : Converts a value from one currency to another using the latest exchange rate.    
	Parameters:
	amount (int): The amount of money to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_currency (str): The currency to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_currency (str): The currency to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	live_conversion (bool): If true, use the latest exchange rate for conversion, else use the last known rate. Default is true.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [amount,from_currency,to_currency,]

	"""
	return 'Success'

tools = [unit_conversion_convert, currency_exchange_convert]
