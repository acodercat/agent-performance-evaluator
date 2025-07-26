from typing import List, Dict, Any, Union, Tuple, Set 
def geometry_calculate_cone_volume(radius:float, height:float, round_off:int=2) -> str:
	"""
	geometry_calculate_cone_volume : Calculate the volume of a cone given the radius and height.    
	Parameters:
	radius (float): Radius of the cone base.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (float): Height of the cone.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	round_off (int): Number of decimal places to round off the answer.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [radius,height,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def physics_calculate_cone_mass(radius:float, height:float, density:float) -> str:
	"""
	physics_calculate_cone_mass : Calculate the mass of a cone given the radius, height, and density.    
	Parameters:
	radius (float): Radius of the cone base.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (float): Height of the cone.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	density (float): Density of the material the cone is made of.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [radius,height,density,]

	"""
	return 'Success'

tools = [geometry_calculate_cone_volume, physics_calculate_cone_mass]
