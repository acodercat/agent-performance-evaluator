from typing import List, Dict, Any, Union, Tuple, Set 
def cosine_similarity_calculate(vector1:List[int], vector2:List[int], rounding:int=None) -> str:
	"""
	cosine_similarity_calculate : Calculate the cosine similarity between two vectors.    
	Parameters:
	vector1 (List[int]): The first vector for calculating cosine similarity.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	vector2 (List[int]): The second vector for calculating cosine similarity.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rounding (int): Optional: The number of decimals to round off the result. Default 0
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [vector1,vector2,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def correlation_calculate(array1:List[int], array2:List[int], type:str=None) -> str:
	"""
	correlation_calculate : Calculate the correlation coefficient between two arrays of numbers.    
	Parameters:
	array1 (List[int]): The first array of numbers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	array2 (List[int]): The second array of numbers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Optional: The type of correlation coefficient to calculate. Default is 'pearson'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [array1,array2,]

	"""
	return 'Success'

tools = [cosine_similarity_calculate, correlation_calculate]
