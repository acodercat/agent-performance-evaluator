from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_density(country:str, year:str, population:int, land_area:float) -> str:
	"""
	calculate_density : Calculate the population density of a specific country in a specific year.    
	Parameters:
	country (str): The country for which the density needs to be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (str): The year in which the density is to be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	population (int): The population of the country.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	land_area (float): The land area of the country in square kilometers.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [country,year,population,land_area,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def crime_record_get_record(case_number:str, county:str, details:bool=None) -> str:
	"""
	crime_record_get_record : Retrieve detailed felony crime records using a specific case number and location.    
	Parameters:
	case_number (str): The case number related to the crime.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	county (str): The county in which the crime occurred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	details (bool): To get a detailed report, set as true. Defaults to false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,county,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_highest_scoring_player(game:str, season:str, region:str=None) -> str:
	"""
	get_highest_scoring_player : Retrieve the highest scoring player in a specific game and season.    
	Parameters:
	game (str): The game in which you want to find the highest scoring player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): The season during which the high score was achieved.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): The geographical region in which the game is being played (Optional). Defaults to 'USA'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game,season,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_compound_interest(principle:float, interest_rate:float, time:int, compounds_per_year:int=None) -> str:
	"""
	calculate_compound_interest : Calculates the compound interest of an investment over a given time period.    
	Parameters:
	principle (float): The initial amount of the investment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	interest_rate (float): The yearly interest rate of the investment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The time, in years, the money is invested or borrowed for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	compounds_per_year (int): The number of times the interest is compounded per year. Default is 1 (interest is compounded yearly).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle,interest_rate,time,]

	"""
	return 'Success'

tools = [calculate_density, crime_record_get_record, get_highest_scoring_player, calculate_compound_interest]
