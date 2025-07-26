from typing import List, Dict, Any, Union, Tuple, Set 
def car_rental(location:str, car_type:List[str], fuel_type:str=None) -> str:
	"""
	car_rental : Rent a car near you based on your preference.    
	Parameters:
	location (str): Your location
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	car_type (List[str]): Type of cars that you want to rent.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	fuel_type (str): Preferred fuel type of car. Gas, diesel, electric, hybrid etc. Default 'gas'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,car_type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawyer_finder(location:str, specialization:List[str], experience:int=None) -> str:
	"""
	lawyer_finder : Locate lawyers near you based on their specialization.    
	Parameters:
	location (str): Your location
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specialization (List[str]): Specializations of lawyer that you are looking for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	experience (int): Experience in years that lawyer has. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,specialization,]

	"""
	return 'Success'

tools = [car_rental, lawyer_finder]
