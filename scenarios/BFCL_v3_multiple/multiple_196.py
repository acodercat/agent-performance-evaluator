def locate_tallest_mountains(location, radius, amount):
	"""
	Find the tallest mountains within a specified radius of a location.    
	Parameters:
	location: The city from which to calculate distance.
	radius: The radius within which to find mountains, measured in kilometers.
	amount: The number of mountains to find, listed from tallest to smallest.

	"""
	pass

def calculate_electric_field(charge, distance, permitivity=None):
	"""
	Calculate the electric field produced by a charge at a certain distance.    
	Parameters:
	charge: Charge in coulombs producing the electric field.
	distance: Distance from the charge in meters where the field is being measured.
	permitivity: Permitivity of the space where field is being calculated, default is for vacuum.

	"""
	pass

def calculate_genotype_frequency(allele_frequency, genotype):
	"""
	Calculate the frequency of homozygous dominant genotype based on the allele frequency using Hardy Weinberg Principle.    
	Parameters:
	allele_frequency: The frequency of the dominant allele in the population.
	genotype: The genotype which frequency is needed, default is homozygous dominant. 

	"""
	pass

def cellbio_get_proteins(cell_compartment, include_description='false'):
	"""
	Get the list of proteins in a specific cell compartment.    
	Parameters:
	cell_compartment: The specific cell compartment.
	include_description: Set true if you want a brief description of each protein.

	"""
	pass

tools = [locate_tallest_mountains, calculate_electric_field, calculate_genotype_frequency, cellbio_get_proteins]
