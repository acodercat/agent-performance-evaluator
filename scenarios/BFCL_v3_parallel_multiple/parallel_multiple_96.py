from typing import List, Dict, Any, Union, Tuple, Set 
def library_find_nearby(location:str, preferences:List[str]) -> str:
	"""
	library_find_nearby : Locate nearby libraries based on specific preferences such as being pet-friendly and having disabled access facilities.    
	Parameters:
	location (str): The city, for example, New York City, NY
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	preferences (List[str]): Your preferences for the library.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,preferences,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def store_find_nearby(location:str, preferences:List[str]) -> str:
	"""
	store_find_nearby : Locate nearby stores based on specific preferences such as being pet-friendly and having disabled access facilities.    
	Parameters:
	location (str): The city, for example, New York City, NY
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	preferences (List[str]): Your preferences for the store.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,preferences,]

	"""
	return 'Success'

tools = [library_find_nearby, store_find_nearby]
