from typing import List, Dict, Any, Union, Tuple, Set 
def electric_field_calculate(Q:float, r:float) -> str:
	"""
	electric_field_calculate : Calculate the electric field based on the amount of charge and distance from the charge    
	Parameters:
	Q (float): The amount of charge in coulombs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	r (float): The distance from the charge in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [Q,r,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def magnetic_field_calculate(I:int, r:float) -> str:
	"""
	magnetic_field_calculate : Calculate the magnetic field based on the current flowing and the radial distance using Ampere’s law    
	Parameters:
	I (int): The electric current flowing in Amperes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	r (float): The radial distance from the line of current in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [I,r,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def electric_force_calculate(Q1:float, Q2:float, r:float) -> str:
	"""
	electric_force_calculate : Calculate the electric force between two charges at a distance    
	Parameters:
	Q1 (float): The amount of the first charge in coulombs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	Q2 (float): The amount of the second charge in coulombs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	r (float): The distance between the two charges in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [Q1,Q2,r,]

	"""
	return 'Success'

tools = [electric_field_calculate, magnetic_field_calculate, electric_force_calculate]
