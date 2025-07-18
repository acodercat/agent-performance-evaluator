from typing import List, Dict, Any, Union, Tuple 
def library_find_nearby(location:str, preferences:List[str]):
	"""
	library_find_nearby : Locate nearby libraries based on specific preferences such as being pet-friendly and having disabled access facilities.    
	Parameters:
	location (str): The city, for example, New York City, NY
	preferences (List[str]): Your preferences for the library.

	Required Parameter = [location,preferences,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def store_find_nearby(location:str, preferences:List[str]):
	"""
	store_find_nearby : Locate nearby stores based on specific preferences such as being pet-friendly and having disabled access facilities.    
	Parameters:
	location (str): The city, for example, New York City, NY
	preferences (List[str]): Your preferences for the store.

	Required Parameter = [location,preferences,]

	"""
	pass

tools = [library_find_nearby, store_find_nearby]
