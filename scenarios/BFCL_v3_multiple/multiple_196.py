from typing import List, Dict, Any, Union, Tuple, Set 
def locate_tallest_mountains(location:str, radius:float, amount:int) -> str:
	"""
	locate_tallest_mountains : Find the tallest mountains within a specified radius of a location.    
	Parameters:
	location (str): The city from which to calculate distance.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	radius (float): The radius within which to find mountains, measured in kilometers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (int): The number of mountains to find, listed from tallest to smallest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,radius,amount,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_electric_field(charge:float, distance:float, permitivity:float=None) -> str:
	"""
	calculate_electric_field : Calculate the electric field produced by a charge at a certain distance.    
	Parameters:
	charge (float): Charge in coulombs producing the electric field.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	distance (float): Distance from the charge in meters where the field is being measured.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	permitivity (float): Permitivity of the space where field is being calculated, default is for vacuum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [charge,distance,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_genotype_frequency(allele_frequency:float, genotype:str) -> str:
	"""
	calculate_genotype_frequency : Calculate the frequency of homozygous dominant genotype based on the allele frequency using Hardy Weinberg Principle.    
	Parameters:
	allele_frequency (float): The frequency of the dominant allele in the population.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	genotype (str): The genotype which frequency is needed, default is homozygous dominant. 
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [allele_frequency,genotype,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def cellbio_get_proteins(cell_compartment:str, include_description:bool='false') -> str:
	"""
	cellbio_get_proteins : Get the list of proteins in a specific cell compartment.    
	Parameters:
	cell_compartment (str): The specific cell compartment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_description (bool): Set true if you want a brief description of each protein.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [cell_compartment,]

	"""
	return 'Success'

tools = [locate_tallest_mountains, calculate_electric_field, calculate_genotype_frequency, cellbio_get_proteins]
