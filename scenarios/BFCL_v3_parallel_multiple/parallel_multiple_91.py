from typing import List, Dict, Any, Union, Tuple, Set 
def biological_calc_biomass(energy:float, efficiency:float=0.1) -> str:
	"""
	biological_calc_biomass : Calculate the biomass from the energy given the energy conversion efficiency.    
	Parameters:
	energy (float): The total energy produced.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	efficiency (float): The conversion efficiency, default value is 10%.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [energy,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def biological_calc_energy(mols:float, substance:str, joules_per_mol:float=2800.0) -> str:
	"""
	biological_calc_energy : Calculate energy from amount of substance based on its molecular composition.    
	Parameters:
	mols (float): Amount of substance in moles.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	substance (str): The chemical formula of the substance.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	joules_per_mol (float): The energy produced or required for the reaction, default value for glucose is 2800 kJ/mol
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [mols,substance,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def physical_calc_work(energy:float, distance:float) -> str:
	"""
	physical_calc_work : Calculate the work from energy.    
	Parameters:
	energy (float): The total energy produced.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	distance (float): The distance over which the work is done.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [energy,distance,]

	"""
	return 'Success'

tools = [biological_calc_biomass, biological_calc_energy, physical_calc_work]
