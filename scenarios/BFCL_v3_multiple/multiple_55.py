from typing import List, Dict, Any, Union, Tuple, Set 
def stock_forecast(company:str, days:int, model:str=None) -> str:
	"""
	stock_forecast : Predict the future stock price for a specific company and time frame.    
	Parameters:
	company (str): The company that you want to get the stock price prediction for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of future days for which to predict the stock price.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	model (str): The model to use for prediction. Default 'regression'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def weather_forecast(location:str, days:int) -> str:
	"""
	weather_forecast : Retrieve a weather forecast for a specific location and time frame.    
	Parameters:
	location (str): The city that you want to get the weather for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of days for the forecast.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,days,]

	"""
	return 'Success'

tools = [stock_forecast, weather_forecast]
