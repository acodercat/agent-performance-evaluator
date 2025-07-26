from typing import List, Dict, Any, Union, Tuple, Set 
def integral(function:str, a:float, b:float) -> str:
	"""
	integral : Calculate the definite integral of a function over an interval [a, b].    
	Parameters:
	function (str): The function to integrate.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	a (float): The lower bound of the interval.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	b (float): The upper bound of the interval.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [function,a,b,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def derivative(function:str, x:float) -> str:
	"""
	derivative : Find the derivative of a function at a certain point.    
	Parameters:
	function (str): The function to differentiate.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	x (float): The point to calculate the derivative at.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [function,x,]

	"""
	return 'Success'

tools = [integral, derivative]
