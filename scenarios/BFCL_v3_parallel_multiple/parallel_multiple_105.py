from typing import List, Dict, Any, Union, Tuple, Set 
def flights_search(from_city:str, to_city:str, date:str=None) -> str:
	"""
	flights_search : Find flights between two cities.    
	Parameters:
	from_city (str): The city to depart from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_city (str): The city to arrive at.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date to fly. Default is today if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [from_city,to_city,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def timezones_get_difference(city1:str, city2:str) -> str:
	"""
	timezones_get_difference : Find the time difference between two cities.    
	Parameters:
	city1 (str): The first city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city2 (str): The second city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city1,city2,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def geodistance_find(origin:str, destination:str, unit:str='miles') -> str:
	"""
	geodistance_find : Find the distance between two cities on the globe.    
	Parameters:
	origin (str): The originating city for the distance calculation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): The destination city for the distance calculation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The unit of measure for the distance calculation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [origin,destination,]

	"""
	return 'Success'

tools = [flights_search, timezones_get_difference, geodistance_find]
