from typing import List, Dict, Any, Union, Tuple, Set 
def get_theater_movie_releases(location:str, timeframe:int, format:str='IMAX') -> str:
	"""
	get_theater_movie_releases : Retrieve the list of movie releases in specific theaters for a specified period.    
	Parameters:
	location (str): The location of the theaters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	timeframe (int): The number of days for which releases are required from current date.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	format (str): Format of movies - could be 'IMAX', '2D', '3D', '4DX' etc. This is an optional parameter.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,timeframe,]

	"""
	return 'Success'

tools = [get_theater_movie_releases]
