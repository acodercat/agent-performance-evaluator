from typing import List, Dict, Any, Union, Tuple, Set 
def get_air_quality(location:str, detail:bool=None) -> str:
	"""
	get_air_quality : Retrieve real-time air quality and pollution data for a specific location.    
	Parameters:
	location (str): The city that you want to get the air quality data for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detail (bool): If true, additional data like PM2.5, PM10, ozone levels, and pollution sources will be retrieved. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

tools = [get_air_quality]
