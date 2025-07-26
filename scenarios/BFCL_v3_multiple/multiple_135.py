from typing import List, Dict, Any, Union, Tuple, Set 
def get_case_info(docket:str, court:str, info_type:str) -> str:
	"""
	get_case_info : Retrieve case details using a specific case docket number and court location.    
	Parameters:
	docket (str): Docket number for the specific court case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	court (str): Court in which the case was heard.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	info_type (str): Specify the information type needed for the case. i.e., victim, accused, verdict etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [docket,court,info_type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_triangle_area(base:float, height:float, unit:str=None) -> str:
	"""
	calculate_triangle_area : Calculate the area of a triangle given its base and height.    
	Parameters:
	base (float): The base of the triangle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (float): The height of the triangle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	unit (str): The unit of measure (defaults to 'units' if not specified)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [base,height,]

	"""
	return 'Success'

tools = [get_case_info, calculate_triangle_area]
