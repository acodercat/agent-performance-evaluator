from typing import List, Dict, Any, Union, Tuple, Set 
def car_rental(location:str, car_type:List[str], fuel_type:str=None):
	"""
	car_rental : Rent a car near you based on your preference.    
	Parameters:
	location (str): Your location
	car_type (List[str]): Type of cars that you want to rent.
	fuel_type (str): Preferred fuel type of car. Gas, diesel, electric, hybrid etc. Default 'gas'

	Required Parameter = [location,car_type,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def lawyer_finder(location:str, specialization:List[str], experience:int=None):
	"""
	lawyer_finder : Locate lawyers near you based on their specialization.    
	Parameters:
	location (str): Your location
	specialization (List[str]): Specializations of lawyer that you are looking for.
	experience (int): Experience in years that lawyer has. Default 1

	Required Parameter = [location,specialization,]

	"""
	pass

tools = [car_rental, lawyer_finder]
