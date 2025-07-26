from typing import List, Dict, Any, Union, Tuple, Set 
def database_us_census_get_population(area:str, type:str, year:int=2000) -> str:
	"""
	database_us_census_get_population : Fetch population data from US Census database.    
	Parameters:
	area (str): Name of the city, state, or country.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Specify whether the area is city/state/country.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year of the data
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [area,type,]

	"""
	return 'Success'

tools = [database_us_census_get_population]
