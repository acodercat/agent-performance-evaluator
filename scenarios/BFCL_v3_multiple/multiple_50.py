def house_price_forecast(location, months, features=None):
	"""
	Predict the house prices for a specific location and time frame.    
	Parameters:
	location: The city that you want to get the house price prediction for.
	months: Number of future months for the prediction.
	features: Additional features considered for prediction. Not required. Default empty array

	"""
	pass

def weather_forecast(location, days):
	"""
	Retrieve a weather forecast for a specific location and time frame.    
	Parameters:
	location: The city that you want to get the weather for.
	days: Number of days for the forecast.

	"""
	pass

def stock_market_forecast(company, days):
	"""
	Predict the stock prices for a specific company and time frame.    
	Parameters:
	company: The company that you want to get the stock price prediction for.
	days: Number of future days for the prediction.

	"""
	pass

tools = [house_price_forecast, weather_forecast, stock_market_forecast]
