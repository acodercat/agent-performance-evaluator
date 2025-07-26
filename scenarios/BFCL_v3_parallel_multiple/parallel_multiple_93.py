from typing import List, Dict, Any, Union, Tuple, Set 
def geology_get_era(era_name:str, calculate_years_ago:bool=None) -> str:
	"""
	geology_get_era : Get the estimated date of a geological era.    
	Parameters:
	era_name (str): The name of the geological era. e.g Ice age
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	calculate_years_ago (bool): True if years ago is to be calculated. False by default
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [era_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def history_get_event_date(event_name:str, calculate_years_ago:bool=None) -> str:
	"""
	history_get_event_date : Get the date of an historical event.    
	Parameters:
	event_name (str): The name of the event.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	calculate_years_ago (bool): True if years ago is to be calculated. False by default
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [event_name,]

	"""
	return 'Success'

tools = [geology_get_era, history_get_event_date]
