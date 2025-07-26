from typing import List, Dict, Any, Union, Tuple, Set 
def museum_get_hours(museum_name:str) -> str:
	"""
	museum_get_hours : Retrieve the operational hours of a specified museum.    
	Parameters:
	museum_name (str): The name of the museum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def location_get_travel_time(destination:str, mode:str='Driving') -> str:
	"""
	location_get_travel_time : Retrieve the estimated travel time from current location to a specific destination.    
	Parameters:
	destination (str): The destination location.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mode (str): Mode of travel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [destination,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def museum_get_waiting_time(museum_name:str, day:str='Monday') -> str:
	"""
	museum_get_waiting_time : Retrieve the estimated waiting time at a specific museum.    
	Parameters:
	museum_name (str): The name of the museum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	day (str): Day of the week.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum_name,]

	"""
	return 'Success'

tools = [museum_get_hours, location_get_travel_time, museum_get_waiting_time]
