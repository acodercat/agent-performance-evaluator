def windFarm_potential(coordinates, turbineCount, month=''):
	"""
	Estimate the energy output of a wind farm given its location and turbine count for a particular month.    
	Parameters:
	coordinates: The geographic coordinates of the location of the wind farm.
	turbineCount: The total number of wind turbines at the location.
	month: The month for which to calculate the potential energy output.

	"""
	pass

def solarFarm_potential(coordinates, panelArea, month=''):
	"""
	Estimate the energy output of a solar farm given its location and panel area for a particular month.    
	Parameters:
	coordinates: The geographic coordinates of the location of the solar farm.
	panelArea: The total solar panel area in square feet at the location.
	month: The month for which to calculate the potential energy output.

	"""
	pass

tools = [windFarm_potential, solarFarm_potential]
