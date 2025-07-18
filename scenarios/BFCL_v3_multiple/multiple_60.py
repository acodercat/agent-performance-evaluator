from typing import List, Dict, Any, Union, Tuple 
def event_search(location:str, days:int):
	"""
	event_search : Search for events happening in a specific location for a future date.    
	Parameters:
	location (str): The city that you want to get the event information for.
	days (int): Number of future days for which to retrieve the event information.

	Required Parameter = [location,days,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def movie_showtimes(location:str, days:int):
	"""
	movie_showtimes : Retrieve movie showtimes for a specific location and for a future date.    
	Parameters:
	location (str): The city that you want to get the movie showtimes for.
	days (int): Number of future days for which to retrieve the showtimes.

	Required Parameter = [location,days,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def humidity_temperature_forecast(location:str, days:int):
	"""
	humidity_temperature_forecast : Retrieve forecast of humidity and temperature for a specific location and for a future date.    
	Parameters:
	location (str): The city that you want to get the humidity and temperature forecast for.
	days (int): Number of future days for which to retrieve the forecast.

	Required Parameter = [location,days,]

	"""
	pass

tools = [event_search, movie_showtimes, humidity_temperature_forecast]
