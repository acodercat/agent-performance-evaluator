from typing import List, Dict, Any, Union, Tuple, Set 
def resistance_calculator_calculate(I:float, V:float) -> str:
	"""
	resistance_calculator_calculate : Calculate the resistance of an electrical circuit based on current and voltage.    
	Parameters:
	I (float): The electric current flowing in Amperes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	V (float): The voltage difference in Volts.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [I,V,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def capacitance_calculator_calculate(A:int, d:float, K:float=None) -> str:
	"""
	capacitance_calculator_calculate : Calculate the capacitance of a parallel plate capacitor based on the area, distance and dielectric constant using the equation C = ε₀KA/d.    
	Parameters:
	A (int): The area of one plate of the capacitor in square meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	d (float): The distance between the two plates in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	K (float): The dielectric constant (default is 1.0 for free space, optional).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [A,d,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def magnetic_field_calculate(I:float, r:float) -> str:
	"""
	magnetic_field_calculate : Calculate the magnetic field based on the current flowing and the radial distance.    
	Parameters:
	I (float): The electric current flowing in Amperes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	r (float): The radial distance from the line of current in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [I,r,]

	"""
	return 'Success'

tools = [resistance_calculator_calculate, capacitance_calculator_calculate, magnetic_field_calculate]
