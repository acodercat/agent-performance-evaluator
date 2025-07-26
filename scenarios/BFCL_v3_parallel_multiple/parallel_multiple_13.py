from typing import List, Dict, Any, Union, Tuple, Set 
def temperature_converter_convert(temperature:float, from_unit:str, to_unit:str, round_to:int=None) -> str:
	"""
	temperature_converter_convert : Convert a temperature from one unit to another.    
	Parameters:
	temperature (float): The temperature to convert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_unit (str): The unit to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_unit (str): The unit to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	round_to (int): The number of decimal places to round the result to. Defaults to 2.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [temperature,from_unit,to_unit,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def energy_calculator_calculate(substance:str, mass:float, initial_temperature:float, final_temperature:float, unit:str=None) -> str:
	"""
	energy_calculator_calculate : Calculate the energy needed to heat a substance from an initial to a final temperature.    
	Parameters:
	substance (str): The substance to be heated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mass (float): The mass of the substance in grams.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	initial_temperature (float): The initial temperature of the substance in degrees Celsius.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	final_temperature (float): The final temperature of the substance in degrees Celsius.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The unit to report the energy in. Options are 'joules' and 'calories'. Defaults to 'joules'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [substance,mass,initial_temperature,final_temperature,]

	"""
	return 'Success'

tools = [temperature_converter_convert, energy_calculator_calculate]
