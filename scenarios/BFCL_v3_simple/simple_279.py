from typing import List, Dict, Any, Union, Tuple, Set 
def instrument_price_get(brand:str, model:str, finish:str) -> str:
	"""
	instrument_price_get : Retrieve the current retail price of a specific musical instrument.    
	Parameters:
	brand (str): The brand of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	model (str): The specific model of the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	finish (str): The color or type of finish on the instrument.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [brand,model,finish,]

	"""
	return 'Success'

tools = [instrument_price_get]
