def calculate_cell_density(optical_density, dilution, calibration_factor=None):
	"""
	Calculate the cell density of a biological sample based on its optical density and the experiment dilution.    
	Parameters:
	optical_density: The optical density of the sample, usually obtained from a spectrophotometer reading.
	dilution: The dilution factor applied during the experiment.
	calibration_factor: The calibration factor to adjust the density, default value is 1e9 assuming cell density is in CFU/mL.

	"""
	pass

tools = [calculate_cell_density]
