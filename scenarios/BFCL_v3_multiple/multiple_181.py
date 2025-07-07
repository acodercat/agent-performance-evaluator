def building_get_dimensions(building_name, unit):
	"""
	Retrieve the dimensions of a specific building based on its name.    
	Parameters:
	building_name: The name of the building.
	unit: The unit in which you want the dimensions. Default is meter.

	"""
	pass

def plot_sine_wave(start_range, end_range, frequency, amplitude=None, phase_shift=None):
	"""
	Plot a sine wave for a given frequency in a given range.    
	Parameters:
	start_range: Start of the range in radians.
	end_range: End of the range in radians.
	frequency: Frequency of the sine wave in Hz.
	amplitude: Amplitude of the sine wave. Default is 1.
	phase_shift: Phase shift of the sine wave in radians. Default is 0.

	"""
	pass

def random_forest_train(n_estimators, max_depth, data):
	"""
	Train a Random Forest Model on given data    
	Parameters:
	n_estimators: The number of trees in the forest.
	max_depth: The maximum depth of the tree.
	data: The training data for the model.

	"""
	pass

def soccer_get_last_match(team_name, include_stats=None):
	"""
	Retrieve the details of the last match played by a specified soccer club.    
	Parameters:
	team_name: The name of the soccer club.
	include_stats: If true, include match statistics like possession, shots on target etc. Default is false.

	"""
	pass

tools = [building_get_dimensions, plot_sine_wave, random_forest_train, soccer_get_last_match]
