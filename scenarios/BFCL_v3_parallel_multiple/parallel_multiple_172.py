from typing import List, Dict, Any, Union, Tuple, Set 
def grocery_store_find_best(my_location:str, products:List[str], rating:float=None) -> str:
	"""
	grocery_store_find_best : Find the closest high-rated grocery stores based on certain product availability.    
	Parameters:
	my_location (str): The current location of the user.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rating (float): The minimum required store rating. Default is 5.0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	products (List[str]): Required products in a list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [my_location,products,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_emissions(distance:int, fuel_type:str, fuel_efficiency:int, efficiency_reduction:int=None) -> str:
	"""
	calculate_emissions : Calculates the annual carbon dioxide emissions produced by a vehicle based on the distance traveled, the fuel type and the fuel efficiency of the vehicle.    
	Parameters:
	distance (int): The distance travelled in miles.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	fuel_type (str): Type of fuel used by the vehicle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	fuel_efficiency (int): The vehicle's fuel efficiency in miles per gallon.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	efficiency_reduction (int): The percentage decrease in fuel efficiency per year (optional). Default is 0
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [distance,fuel_type,fuel_efficiency,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sculpture_get_details(artist:str, title:str, detail:str=None) -> str:
	"""
	sculpture_get_details : Retrieve details of a sculpture based on the artist and the title of the sculpture.    
	Parameters:
	artist (str): The artist who made the sculpture.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	title (str): The title of the sculpture.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detail (str): The specific detail wanted about the sculpture. Default is 'general information'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [artist,title,]

	"""
	return 'Success'

tools = [grocery_store_find_best, calculate_emissions, sculpture_get_details]
