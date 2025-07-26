from typing import List, Dict, Any, Union, Tuple, Set 
def crime_statute_lookup(jurisdiction:str, crime:str, detail_level:str=None) -> str:
	"""
	crime_statute_lookup : Look up the criminal statutes in a specific jurisdiction to find possible punishments for a specific crime.    
	Parameters:
	jurisdiction (str): The jurisdiction to search in, usually a state or country.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	crime (str): The crime to search for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	detail_level (str): How detailed of a report to return. Optional, default is 'basic'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [jurisdiction,crime,]

	"""
	return 'Success'

tools = [crime_statute_lookup]
