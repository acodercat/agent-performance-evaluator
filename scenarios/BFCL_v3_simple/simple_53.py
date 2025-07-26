from typing import List, Dict, Any, Union, Tuple, Set 
def fetch_DNA_sequence(DNA_id:str, format:str=None, upstream:int=None) -> str:
	"""
	fetch_DNA_sequence : Retrieve the sequence of a DNA molecule with the given id from a public database.    
	Parameters:
	DNA_id (str): Unique ID of the DNA molecule in the database.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	format (str): Optional parameter to get sequence in specific format (default to 'fasta').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	upstream (int): Optional parameter to include certain number of base pairs upstream the DNA sequence (default to 0).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [DNA_id,]

	"""
	return 'Success'

tools = [fetch_DNA_sequence]
