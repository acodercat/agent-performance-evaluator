from typing import List, Dict, Any, Union, Tuple, Set 
def thermo_calculate_energy(mass:int, phase_transition:str, substance:str=None) -> str:
	"""
	thermo_calculate_energy : Calculate the energy required or released during a phase change using mass, the phase transition temperature and the specific latent heat.    
	Parameters:
	mass (int): Mass of the substance in grams.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	phase_transition (str): Phase transition. Can be 'melting', 'freezing', 'vaporization', 'condensation'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	substance (str): The substance which is undergoing phase change, default is 'water'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [mass,phase_transition,]

	"""
	return 'Success'

tools = [thermo_calculate_energy]
