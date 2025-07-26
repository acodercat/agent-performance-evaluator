from typing import List, Dict, Any, Union, Tuple, Set 
def history_get_timeline(event:str, region:str='Europe') -> str:
	"""
	history_get_timeline : Retrieve the timeline for a specific historical event    
	Parameters:
	event (str): The historical event you want the timeline for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): Region of the event.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [event,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def history_get_important_figures(event:str, number:int=1) -> str:
	"""
	history_get_important_figures : Retrieve array of important figures involved during a specific historical event.    
	Parameters:
	event (str): The historical event for which you want the array of important figures.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number (int): Number of top figures you want. Default to 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [event,]

	"""
	return 'Success'

tools = [history_get_timeline, history_get_important_figures]
