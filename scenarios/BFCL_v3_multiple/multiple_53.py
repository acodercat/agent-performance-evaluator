def linear_regression(independent_var, dependent_var, forecast_period=None):
	"""
	Applies linear regression to a given set of independent variables to make a prediction.    
	Parameters:
	independent_var: The independent variables.
	dependent_var: The dependent variable.
	forecast_period: The number of years to forecast the prices. Default 1

	"""
	pass

def random_forest_regression(independent_var, dependent_var, n_estimators=None, forecast_period=None):
	"""
	Applies Random Forest Regression to a given set of independent variables to make a prediction.    
	Parameters:
	independent_var: The independent variables.
	dependent_var: The dependent variable.
	n_estimators: The number of trees in the forest. Default 1
	forecast_period: The number of years to forecast the prices. Default 1

	"""
	pass

tools = [linear_regression, random_forest_regression]
