from typing import List, Dict, Any, Union, Tuple, Set 
def sculpture_create_custom(item:str, material:str, size:int=None) -> str:
	"""
	sculpture_create_custom : Order a custom sculpture with your preferred material.    
	Parameters:
	item (str): The subject of the sculpture, e.g. horse
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	material (str): Preferred material for the sculpture.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	size (int): The desired size for the sculpture in inches. This parameter is optional. Default is 10 inches if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [item,material,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def painting_create_custom(subject:str, color:str, size:int=None) -> str:
	"""
	painting_create_custom : Order a custom painting with your preferred color.    
	Parameters:
	subject (str): The subject of the painting, e.g. horse
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	color (str): Preferred main color for the painting.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	size (int): The desired size for the painting in inches. This parameter is optional. Default is 20 inches if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [subject,color,]

	"""
	return 'Success'

tools = [sculpture_create_custom, painting_create_custom]
