from typing import List, Dict, Any, Union, Tuple 
def house_price_forecast(location:str, months:int, features:List[str]=None):
	"""
	house_price_forecast : Predict the house prices for a specific location and time frame.    
	Parameters:
	location (str): The city that you want to get the house price prediction for.
	months (int): Number of future months for the prediction.
	features (List[str]): Additional features considered for prediction. Not required. Default empty array

	Required Parameter = [location,months,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def weather_forecast(location:str, days:int):
	"""
	weather_forecast : Retrieve a weather forecast for a specific location and time frame.    
	Parameters:
	location (str): The city that you want to get the weather for.
	days (int): Number of days for the forecast.

	Required Parameter = [location,days,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def stock_market_forecast(company:str, days:int):
	"""
	stock_market_forecast : Predict the stock prices for a specific company and time frame.    
	Parameters:
	company (str): The company that you want to get the stock price prediction for.
	days (int): Number of future days for the prediction.

	Required Parameter = [company,days,]

	"""
	pass

tools = [house_price_forecast, weather_forecast, stock_market_forecast]
