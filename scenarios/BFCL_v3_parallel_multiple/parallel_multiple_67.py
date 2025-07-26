from typing import List, Dict, Any, Union, Tuple, Set 
def math_roots_polynomial(coefficients:List[float], degree:float=4) -> str:
	"""
	math_roots_polynomial : Calculate the roots of a polynomial equation.    
	Parameters:
	coefficients (List[float]): Array of coefficients of the polynomial equation starting from highest degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	degree (float): Degree of the polynomial equation.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [coefficients,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def math_roots_cubic(a:float, b:float, c:float, d:float) -> str:
	"""
	math_roots_cubic : Calculate the roots of a cubic equation.    
	Parameters:
	a (float): Coefficient of the third-degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	b (float): Coefficient of the second-degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	c (float): Coefficient of the first-degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	d (float): Constant term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [a,b,c,d,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def math_roots_quadratic(a:float, b:float, c:float) -> str:
	"""
	math_roots_quadratic : Calculate the roots of a quadratic equation.    
	Parameters:
	a (float): Coefficient of the second-degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	b (float): Coefficient of the first-degree term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	c (float): Constant term.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [a,b,c,]

	"""
	return 'Success'

tools = [math_roots_polynomial, math_roots_cubic, math_roots_quadratic]
