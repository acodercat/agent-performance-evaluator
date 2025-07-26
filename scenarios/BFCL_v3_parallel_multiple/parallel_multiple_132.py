from typing import List, Dict, Any, Union, Tuple, Set 
def calculus_derivative(function:str, value:int, function_variable:str=None) -> str:
	"""
	calculus_derivative : Compute the derivative of a function at a specific value.    
	Parameters:
	function (str): The function to calculate the derivative of.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	value (int): The value where the derivative needs to be calculated at.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	function_variable (str): The variable present in the function, for instance x or y, etc. Default is 'x'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [function,value,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_personality_traits(type:str, traits:List[str]=None) -> str:
	"""
	get_personality_traits : Retrieve the personality traits for a specific personality type, including their strengths and weaknesses.    
	Parameters:
	type (str): The personality type.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	traits (List[str]): List of traits to be retrieved, default is ['strengths', 'weaknesses'].
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [type,]

	"""
	return 'Success'

tools = [calculus_derivative, get_personality_traits]
