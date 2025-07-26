from typing import List, Dict, Any, Union, Tuple, Set 
def doctor_search(location:str, specialization:str) -> str:
	"""
	doctor_search : Search for a doctor based on area of expertise and location    
	Parameters:
	location (str): The city and state, e.g. Los Angeles, CA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specialization (str): Medical specialization. For example, 'Cardiology', 'Orthopedics', 'Gynecology'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,specialization,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawyer_search(location:str, expertise:str) -> str:
	"""
	lawyer_search : Search for a lawyer based on area of expertise and location    
	Parameters:
	location (str): The city and state, e.g. Los Angeles, CA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	expertise (str): Area of legal expertise. For example, 'Marriage', 'Criminal', 'Business'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,expertise,]

	"""
	return 'Success'

tools = [doctor_search, lawyer_search]
