from typing import List, Dict, Any, Union, Tuple, Set 
def us_history_population_by_state_year(state:str, year:int):
	"""
	us_history_population_by_state_year : Retrieve historical population data for a specific U.S. state and year.    
	Parameters:
	state (str): The U.S. state for which to retrieve the population.
	year (int): The year for which to retrieve the population.

	Required Parameter = [state,year,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def us_economy_gdp_by_state_year(state:str, year:int, adjustment:str=None):
	"""
	us_economy_gdp_by_state_year : Retrieve historical GDP data for a specific U.S. state and year.    
	Parameters:
	state (str): The U.S. state for which to retrieve the GDP.
	year (int): The year for which to retrieve the GDP.
	adjustment (str): The type of adjustment for inflation, 'Real' or 'Nominal'. Optional, 'Nominal' by default.

	Required Parameter = [state,year,]

	"""
	pass

tools = [us_history_population_by_state_year, us_economy_gdp_by_state_year]
