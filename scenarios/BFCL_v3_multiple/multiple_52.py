from typing import List, Dict, Any, Union, Tuple, Set 
def unit_conversion(value:float, from_unit:str, to_unit:str) -> str:
	"""
	unit_conversion : Convert a value from one unit to another.    
	Parameters:
	value (float): The value to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_unit (str): The unit to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_unit (str): The unit to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [value,from_unit,to_unit,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def currency_conversion(amount:int, from_currency:str, to_currency:str) -> str:
	"""
	currency_conversion : Convert a value from one currency to another.    
	Parameters:
	amount (int): The amount to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_currency (str): The currency to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_currency (str): The currency to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [amount,from_currency,to_currency,]

	"""
	return 'Success'

tools = [unit_conversion, currency_conversion]
