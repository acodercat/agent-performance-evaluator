from typing import List, Dict, Any, Union, Tuple 
def calculate_cell_density(optical_density:float, dilution:int, calibration_factor:float=None):
	"""
	calculate_cell_density : Calculate the cell density of a biological sample based on its optical density and the experiment dilution.    
	Parameters:
	optical_density (float): The optical density of the sample, usually obtained from a spectrophotometer reading.
	dilution (int): The dilution factor applied during the experiment.
	calibration_factor (float): The calibration factor to adjust the density, default value is 1e9 assuming cell density is in CFU/mL.

	Required Parameter = [optical_density,dilution,]

	"""
	pass

tools = [calculate_cell_density]
