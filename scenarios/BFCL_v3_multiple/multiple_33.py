from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_derivative(func:str, x_value:int, order:int=1) -> str:
	"""
	calculate_derivative : Calculate the derivative of a single-variable function.    
	Parameters:
	func (str): The function to be differentiated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	x_value (int): The x-value at which the derivative should be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	order (int): The order of the derivative (optional). Default is 1st order.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [func,x_value,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_integral(func:str, a:int, b:int) -> str:
	"""
	calculate_integral : Calculate the definite integral of a single-variable function.    
	Parameters:
	func (str): The function to be integrated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	a (int): The lower bound of the integration.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	b (int): The upper bound of the integration.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [func,a,b,]

	"""
	return 'Success'

tools = [calculate_derivative, calculate_integral]
