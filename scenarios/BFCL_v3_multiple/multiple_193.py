from typing import List, Dict, Any, Union, Tuple, Set 
def math_factorial(number:float) -> str:
	"""
	math_factorial : Calculate the factorial of a given number.    
	Parameters:
	number (float): The number for which factorial needs to be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def grocery_store_find_best(my_location:str, products:List[str], rating:float=None) -> str:
	"""
	grocery_store_find_best : Find the closest high-rated grocery stores based on certain product availability.    
	Parameters:
	my_location (str): The current location of the user.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rating (float): The minimum required store rating. Default is 0.0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	products (List[str]): Required products in a list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [my_location,products,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_find_nearby(location:str, cuisine:str, max_distance:float=None) -> str:
	"""
	restaurant_find_nearby : Locate nearby restaurants based on specific criteria like cuisine type.    
	Parameters:
	location (str): The city and state, e.g. Seattle, WA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cuisine (str): Preferred type of cuisine in restaurant.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	max_distance (float): Maximum distance (in miles) within which to search for restaurants. Default is 5.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,cuisine,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def maps_get_distance_duration(start_location:str, end_location:str, traffic:bool=None) -> str:
	"""
	maps_get_distance_duration : Retrieve the travel distance and estimated travel time from one location to another via car    
	Parameters:
	start_location (str): Starting point of the journey
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end_location (str): Ending point of the journey
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	traffic (bool): If true, considers current traffic. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start_location,end_location,]

	"""
	return 'Success'

tools = [math_factorial, grocery_store_find_best, restaurant_find_nearby, maps_get_distance_duration]
