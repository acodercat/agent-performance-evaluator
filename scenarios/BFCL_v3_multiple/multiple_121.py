from typing import List, Dict, Any, Union, Tuple, Set 
def map_service_get_directions(start:str, end:str, avoid:List[str]=None) -> str:
	"""
	map_service_get_directions : Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start (str): Starting location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end (str): Ending location for the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	avoid (List[str]): Route features to avoid. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start,end,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def science_history_get_invention(invention_name:str, want_year:bool) -> str:
	"""
	science_history_get_invention : Retrieve the inventor and year of invention based on the invention's name.    
	Parameters:
	invention_name (str): The name of the invention.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	want_year (bool): Return the year of invention if set to true.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [invention_name,want_year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def geometry_area_triangle(base:int, height:int, unit:str=None) -> str:
	"""
	geometry_area_triangle : Calculate the area of a triangle.    
	Parameters:
	base (int): The length of the base of the triangle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (int): The height of the triangle from the base.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The measurement unit for the area. Defaults to square meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [base,height,]

	"""
	return 'Success'

tools = [map_service_get_directions, science_history_get_invention, geometry_area_triangle]
