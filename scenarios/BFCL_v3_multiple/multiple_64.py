from typing import List, Dict, Any, Union, Tuple, Set 
def uv_index_get_future(location:str, date:str) -> str:
	"""
	uv_index_get_future : Retrieve UV index data for a specified location and date.    
	Parameters:
	location (str): The location to retrieve the UV index for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date for the UV index, in the format mm-dd-yyyy.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def rainfall_prediction(location:str, date:str) -> str:
	"""
	rainfall_prediction : Retrieve rainfall data for a specified location and date.    
	Parameters:
	location (str): The location to retrieve the rainfall prediction for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date for the rainfall prediction, in the format mm/dd/yyyy.'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def snowfall_prediction(location:str, date:str) -> str:
	"""
	snowfall_prediction : Retrieve snowfall data for a specified location and date.    
	Parameters:
	location (str): The location to retrieve the snowfall prediction for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date for the snowfall prediction, in the format mm-dd-yyyy.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,date,]

	"""
	return 'Success'

tools = [uv_index_get_future, rainfall_prediction, snowfall_prediction]
