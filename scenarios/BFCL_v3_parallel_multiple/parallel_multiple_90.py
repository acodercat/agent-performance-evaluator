from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_final_temperature(quantity1:float, temperature1:float, quantity2:float, temperature2:float) -> str:
	"""
	calculate_final_temperature : Calculate the final temperature when different quantities of the same gas at different temperatures are mixed.    
	Parameters:
	quantity1 (float): The quantity of the first sample of gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	temperature1 (float): The temperature of the first sample of gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	quantity2 (float): The quantity of the second sample of gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	temperature2 (float): The temperature of the second sample of gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [quantity1,temperature1,quantity2,temperature2,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_mass(quantity:float, molar_mass:float) -> str:
	"""
	calculate_mass : Calculate the mass of a gas given its quantity and molar mass.    
	Parameters:
	quantity (float): The quantity of the gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	molar_mass (float): The molar mass of the gas.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [quantity,molar_mass,]

	"""
	return 'Success'

tools = [calculate_final_temperature, calculate_mass]
