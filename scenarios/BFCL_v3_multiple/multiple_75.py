from typing import List, Dict, Any, Union, Tuple, Set 
def weather_forecast(location:str, days:int):
	"""
	weather_forecast : Retrieve a weather forecast for a specific location and time frame.    
	Parameters:
	location (str): The city that you want to get the weather for.
	days (int): Number of days for the forecast.

	Required Parameter = [location,days,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def paint_color_trends(room:str, period:str=None):
	"""
	paint_color_trends : Find the most popular paint color for a specific area in the home.    
	Parameters:
	room (str): Type of the room e.g. Living room, Bathroom etc.
	period (str): The period over which to check the paint color trend. Default 'Daily'

	Required Parameter = [room,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def house_price_trends(location:str, period:str=None):
	"""
	house_price_trends : Find the average house price in a specific area.    
	Parameters:
	location (str): City and state, e.g. New York, NY.
	period (str): The period over which to check the price trend. Default 'Yearly'

	Required Parameter = [location,]

	"""
	pass

tools = [weather_forecast, paint_color_trends, house_price_trends]
