from typing import List, Dict, Any, Union, Tuple, Set 
def get_instrument_details(instrument:str, manufacturer:str, features:List[str]=None) -> str:
	"""
	get_instrument_details : Retrieve the average price and ratings of an instrument from a particular manufacturer.    
	Parameters:
	instrument (str): The name of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	manufacturer (str): The manufacturer of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	features (List[str]): The features to retrieve about the instrument. Default is 'price'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [instrument,manufacturer,]

	"""
	return 'Success'

tools = [get_instrument_details]
