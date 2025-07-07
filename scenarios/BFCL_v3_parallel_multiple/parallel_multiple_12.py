def calculate_voltage_difference(electric_field, distance, charge=0):
	"""
	Calculate the voltage difference between two points in an electric field.    
	Parameters:
	electric_field: The electric field in newtons per coulomb.
	distance: The distance between the two points in the direction of the field in meters.
	charge: The charge of the test particle, typically an electron, in coulombs. Default to 0

	"""
	pass

def calculate_magnetic_field(current, distance, permeability=None):
	"""
	Calculate the magnetic field produced by a current-carrying wire.    
	Parameters:
	current: The current in the wire in amperes.
	distance: The perpendicular distance from the wire in meters.
	permeability: The permeability of free space, a constant value. Default 0.1

	"""
	pass

tools = [calculate_voltage_difference, calculate_magnetic_field]
