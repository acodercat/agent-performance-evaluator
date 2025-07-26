from typing import List, Dict, Any, Union, Tuple, Set 
def unit_conversion_convert(value:float, from_unit:str, to_unit:str) -> str:
	"""
	unit_conversion_convert : Convert a value from one unit to another.    
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
def currency_conversion(amount:float, from_currency:str, to_currency:str) -> str:
	"""
	currency_conversion : Convert a value from one currency to another.    
	Parameters:
	amount (float): The amount to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_currency (str): The currency to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_currency (str): The currency to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [amount,from_currency,to_currency,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_weight_in_space(weight_earth_kg:int, planet:str) -> str:
	"""
	calculate_weight_in_space : Calculate your weight on different planets given your weight on earth    
	Parameters:
	weight_earth_kg (int): Your weight on Earth in Kilograms.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	planet (str): The planet you want to know your weight on.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [weight_earth_kg,planet,]

	"""
	return 'Success'

tools = [unit_conversion_convert, currency_conversion, calculate_weight_in_space]
