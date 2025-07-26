from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_density(mass:int, volume:int, unit:str=None) -> str:
	"""
	calculate_density : Calculate the density of a substance based on its mass and volume.    
	Parameters:
	mass (int): The mass of the substance in kilograms.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	volume (int): The volume of the substance in cubic meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The unit of density. Default is kg/m³
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [mass,volume,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def mix_paint_color(color1:str, color2:str, lightness:int=None) -> str:
	"""
	mix_paint_color : Combine two primary paint colors and adjust the resulting color's lightness level.    
	Parameters:
	color1 (str): The first primary color to be mixed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	color2 (str): The second primary color to be mixed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	lightness (int): The desired lightness level of the resulting color in percentage. The default level is set to 50%.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [color1,color2,]

	"""
	return 'Success'

tools = [calculate_density, mix_paint_color]
