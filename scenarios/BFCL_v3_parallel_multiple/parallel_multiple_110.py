from typing import List, Dict, Any, Union, Tuple, Set 
def us_history_population_by_state_year(state:str, year:int) -> str:
	"""
	us_history_population_by_state_year : Retrieve historical population data for a specific U.S. state and year.    
	Parameters:
	state (str): The U.S. state for which to retrieve the population.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year for which to retrieve the population.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [state,year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def us_economy_gdp_by_state_year(state:str, year:int, adjustment:str=None) -> str:
	"""
	us_economy_gdp_by_state_year : Retrieve historical GDP data for a specific U.S. state and year.    
	Parameters:
	state (str): The U.S. state for which to retrieve the GDP.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year for which to retrieve the GDP.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	adjustment (str): The type of adjustment for inflation, 'Real' or 'Nominal'. Optional, 'Nominal' by default.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [state,year,]

	"""
	return 'Success'

tools = [us_history_population_by_state_year, us_economy_gdp_by_state_year]
