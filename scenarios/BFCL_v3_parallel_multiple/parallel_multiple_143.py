from typing import List, Dict, Any, Union, Tuple, Set 
def find_flute(brand:str, specs:List[str]) -> str:
	"""
	find_flute : Locate a flute for sale based on specific requirements.    
	Parameters:
	brand (str): The brand of the flute. Example, 'Yamaha'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specs (List[str]): The specifications of the flute desired.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [brand,specs,]

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
def math_factorial(number:int) -> str:
	"""
	math_factorial : Calculate the factorial of a given number.    
	Parameters:
	number (int): The number for which factorial needs to be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number,]

	"""
	return 'Success'

tools = [find_flute, calculate_genotype_frequency, math_factorial]
