from typing import List, Dict, Any, Union, Tuple, Set 
def instrument_price_get(brand:str, model:str, finish:str) -> str:
	"""
	instrument_price_get : Retrieve the current retail price of a specific musical instrument.    
	Parameters:
	brand (str): The brand of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	model (str): The specific model of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	finish (str): The color or type of finish on the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [brand,model,finish,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_shortest_driving_distance(origin:str, destination:str, unit:str=None) -> str:
	"""
	get_shortest_driving_distance : Calculate the shortest driving distance between two locations.    
	Parameters:
	origin (str): Starting point of the journey.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): End point of the journey.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): Preferred unit of distance (optional, default is kilometers).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [origin,destination,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def cell_biology_function_lookup(molecule:str, organelle:str, specific_function:bool) -> str:
	"""
	cell_biology_function_lookup : Look up the function of a given molecule in a specified organelle.    
	Parameters:
	molecule (str): The molecule of interest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	organelle (str): The organelle of interest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specific_function (bool): If set to true, a specific function of the molecule within the organelle will be provided, if such information exists.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [molecule,organelle,specific_function,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_scientist_for_discovery(discovery:str) -> str:
	"""
	get_scientist_for_discovery : Retrieve the scientist's name who is credited for a specific scientific discovery or theory.    
	Parameters:
	discovery (str): The scientific discovery or theory.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [discovery,]

	"""
	return 'Success'

tools = [instrument_price_get, get_shortest_driving_distance, cell_biology_function_lookup, get_scientist_for_discovery]
