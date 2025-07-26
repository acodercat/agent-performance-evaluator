from typing import List, Dict, Any, Union, Tuple, Set 
def linear_regression_fit(x:List[float], y:List[float], return_residuals:bool='false') -> str:
	"""
	linear_regression_fit : Fit a linear regression model to data.    
	Parameters:
	x (List[float]): Array of the predictor variable.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	y (List[float]): Array of the dependent variable.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	return_residuals (bool): Flag indicating whether to return the residuals (the difference between the observed and predicted values). Optional.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [x,y,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def data_loading(file_path:str, delimiter:str=',') -> str:
	"""
	data_loading : Load data from a csv file into a data structure.    
	Parameters:
	file_path (str): The path to the file to load.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	delimiter (str): The character used to separate values in the file. Optional.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [file_path,]

	"""
	return 'Success'

tools = [linear_regression_fit, data_loading]
