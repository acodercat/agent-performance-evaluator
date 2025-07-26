from typing import List, Dict, Any, Union, Tuple, Set 
def current_weather_condition(city:str, country:str, measurement:str=None) -> str:
	"""
	current_weather_condition : Get the current weather conditions of a specific city including temperature and humidity.    
	Parameters:
	city (str): The city that you want to get the current weather conditions for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	country (str): The country of the city you specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	measurement (str): You can specify which unit to display the temperature in, 'c' for Celsius, 'f' for Fahrenheit. Default is 'c'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city,country,]

	"""
	return 'Success'

tools = [current_weather_condition]
