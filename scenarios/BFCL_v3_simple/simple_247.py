from typing import List, Dict, Any, Union, Tuple, Set 
def historical_contrib_get_contrib(scientist:str, date:str, category:str=None) -> str:
	"""
	historical_contrib_get_contrib : Retrieve historical contribution made by a scientist on a specific date.    
	Parameters:
	scientist (str): The scientist whose contributions need to be searched.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date when the contribution was made in yyyy-mm-dd format.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	category (str): The field of the contribution, such as 'Physics' or 'Chemistry'. Default is 'all'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [scientist,date,]

	"""
	return 'Success'

tools = [historical_contrib_get_contrib]
