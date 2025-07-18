from typing import List, Dict, Any, Union, Tuple 
def windFarm_potential(coordinates:List[float], turbineCount:float, month:str=''):
	"""
	windFarm_potential : Estimate the energy output of a wind farm given its location and turbine count for a particular month.    
	Parameters:
	coordinates (List[float]): The geographic coordinates of the location of the wind farm.
	turbineCount (float): The total number of wind turbines at the location.
	month (str): The month for which to calculate the potential energy output.

	Required Parameter = [coordinates,turbineCount,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def solarFarm_potential(coordinates:List[float], panelArea:float, month:str=''):
	"""
	solarFarm_potential : Estimate the energy output of a solar farm given its location and panel area for a particular month.    
	Parameters:
	coordinates (List[float]): The geographic coordinates of the location of the solar farm.
	panelArea (float): The total solar panel area in square feet at the location.
	month (str): The month for which to calculate the potential energy output.

	Required Parameter = [coordinates,panelArea,]

	"""
	pass

tools = [windFarm_potential, solarFarm_potential]
