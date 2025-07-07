def weather_get_forecast_by_coordinates(coordinates, days_ahead=None):
	"""
	Get the weather forecast for a specific geographical coordinates.    
	Parameters:
	coordinates: The geographical coordinates for which to retrieve the weather. The first element of the tuple is the latitude and the second is the longitude.
	days_ahead: Number of days to forecast from current date (optional, default is 7).

	"""
	pass

def weather_get_by_coordinates_date(coordinates, date):
	"""
	Retrieves the historical weather data based on coordinates and date.    
	Parameters:
	coordinates: The geographical coordinates for which to retrieve the weather. The first element of the tuple is the latitude and the second is the longitude.
	date: The date for which to retrieve the historical weather data in the format YYYY-MM-DD.

	"""
	pass

def weather_get_by_city_date(city, date):
	"""
	Retrieves the historical weather data based on city and date.    
	Parameters:
	city: The city for which to retrieve the weather.
	date: The date for which to retrieve the historical weather data in the format YYYY-MM-DD.

	"""
	pass

tools = [weather_get_forecast_by_coordinates, weather_get_by_coordinates_date, weather_get_by_city_date]
