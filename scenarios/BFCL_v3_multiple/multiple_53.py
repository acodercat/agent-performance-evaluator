from typing import List, Dict, Any, Union, Tuple, Set 
def linear_regression(independent_var:List[str], dependent_var:str, forecast_period:int=None) -> str:
	"""
	linear_regression : Applies linear regression to a given set of independent variables to make a prediction.    
	Parameters:
	independent_var (List[str]): The independent variables.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dependent_var (str): The dependent variable.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	forecast_period (int): The number of years to forecast the prices. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [independent_var,dependent_var,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def random_forest_regression(independent_var:List[str], dependent_var:str, n_estimators:int=None, forecast_period:int=None) -> str:
	"""
	random_forest_regression : Applies Random Forest Regression to a given set of independent variables to make a prediction.    
	Parameters:
	independent_var (List[str]): The independent variables.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dependent_var (str): The dependent variable.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	n_estimators (int): The number of trees in the forest. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	forecast_period (int): The number of years to forecast the prices. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [independent_var,dependent_var,]

	"""
	return 'Success'

tools = [linear_regression, random_forest_regression]
