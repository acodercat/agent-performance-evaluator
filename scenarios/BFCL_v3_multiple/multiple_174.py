from typing import List, Dict, Any, Union, Tuple, Set 
def sports_ranking(team:str, league:str, season:int=None) -> str:
	"""
	sports_ranking : Fetch the ranking of a specific sports team in a specific league    
	Parameters:
	team (str): The name of the team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): The name of the league.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (int): Optional parameter to specify the season, default is the current season, 2024
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team,league,]

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

tools = [sports_ranking, calculate_compound_interest]
