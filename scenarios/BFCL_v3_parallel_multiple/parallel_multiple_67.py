from typing import List, Dict, Any, Union, Tuple 
def math_roots_polynomial(coefficients:List[float], degree:float=4):
	"""
	math_roots_polynomial : Calculate the roots of a polynomial equation.    
	Parameters:
	coefficients (List[float]): Array of coefficients of the polynomial equation starting from highest degree term.
	degree (float): Degree of the polynomial equation.

	Required Parameter = [coefficients,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def math_roots_cubic(a:float, b:float, c:float, d:float):
	"""
	math_roots_cubic : Calculate the roots of a cubic equation.    
	Parameters:
	a (float): Coefficient of the third-degree term.
	b (float): Coefficient of the second-degree term.
	c (float): Coefficient of the first-degree term.
	d (float): Constant term.

	Required Parameter = [a,b,c,d,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def math_roots_quadratic(a:float, b:float, c:float):
	"""
	math_roots_quadratic : Calculate the roots of a quadratic equation.    
	Parameters:
	a (float): Coefficient of the second-degree term.
	b (float): Coefficient of the first-degree term.
	c (float): Constant term.

	Required Parameter = [a,b,c,]

	"""
	pass

tools = [math_roots_polynomial, math_roots_cubic, math_roots_quadratic]
