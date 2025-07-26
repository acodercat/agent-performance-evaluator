from typing import List, Dict, Any, Union, Tuple, Set 
def filter_list(elements:List[str], condition:str) -> str:
	"""
	filter_list : Filters elements of a list based on a given condition    
	Parameters:
	elements (List[str]): The list of elements to filter.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	condition (str): The condition to filter the elements on.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [elements,condition,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sum_elements(elements:List[int]) -> str:
	"""
	sum_elements : Add all elements of a numeric list    
	Parameters:
	elements (List[int]): The list of numeric elements to add.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [elements,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sort_list(elements:List[str], order:str='asc') -> str:
	"""
	sort_list : Sort the elements of a list in ascending or descending order    
	Parameters:
	elements (List[str]): The list of elements to sort.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	order (str): The order in which to sort the elements. This can be 'asc' for ascending order, or 'desc' for descending order.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [elements,]

	"""
	return 'Success'

tools = [filter_list, sum_elements, sort_list]
