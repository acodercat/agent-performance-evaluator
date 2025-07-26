from typing import List, Dict, Any, Union, Tuple, Set 
def scienceFacts_getCharge(particle:str, unit:str) -> str:
	"""
	scienceFacts_getCharge : Fetch the electric charge of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): Unit to retrieve electric charge. For example, 'coulombs' etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [particle,unit,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def scienceFacts_getWeight(particle:str, unit:str) -> str:
	"""
	scienceFacts_getWeight : Fetch the atomic weight of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): Unit to retrieve weight. For example, 'kg', 'pound', 'amu' etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [particle,unit,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def scienceFacts_getDiameter(particle:str, unit:str) -> str:
	"""
	scienceFacts_getDiameter : Fetch the diameter of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): Unit to retrieve diameter. For example, 'meter', 'cm', 'femtometers' etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [particle,unit,]

	"""
	return 'Success'

tools = [scienceFacts_getCharge, scienceFacts_getWeight, scienceFacts_getDiameter]
