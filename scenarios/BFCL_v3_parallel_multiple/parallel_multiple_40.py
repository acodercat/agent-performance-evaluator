from typing import List, Dict, Any, Union, Tuple 
def scienceFacts_getCharge(particle:str, unit:str):
	"""
	scienceFacts_getCharge : Fetch the electric charge of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
	unit (str): Unit to retrieve electric charge. For example, 'coulombs' etc.

	Required Parameter = [particle,unit,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def scienceFacts_getWeight(particle:str, unit:str):
	"""
	scienceFacts_getWeight : Fetch the atomic weight of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
	unit (str): Unit to retrieve weight. For example, 'kg', 'pound', 'amu' etc.

	Required Parameter = [particle,unit,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def scienceFacts_getDiameter(particle:str, unit:str):
	"""
	scienceFacts_getDiameter : Fetch the diameter of an atomic particle    
	Parameters:
	particle (str): The atomic particle. e.g. Electron, Proton
	unit (str): Unit to retrieve diameter. For example, 'meter', 'cm', 'femtometers' etc.

	Required Parameter = [particle,unit,]

	"""
	pass

tools = [scienceFacts_getCharge, scienceFacts_getWeight, scienceFacts_getDiameter]
