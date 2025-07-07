def calculate_distance(start_point, end_point):
	"""
	Calculate distance between two locations.    
	Parameters:
	start_point: Starting point of the journey.
	end_point: Ending point of the journey.

	"""
	pass

def traffic_estimate(start_location, end_location, time_period=None):
	"""
	Estimate traffic from one location to another for a specific time period.    
	Parameters:
	start_location: Starting location for the journey.
	end_location: Ending location for the journey.
	time_period: Specify a time frame to estimate the traffic, 'now' for current, 'weekend' for the coming weekend. Default 'now'

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

tools = [calculate_distance, traffic_estimate, weather_forecast]
