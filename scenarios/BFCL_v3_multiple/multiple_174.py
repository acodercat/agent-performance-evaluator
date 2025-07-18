from typing import List, Dict, Any, Union, Tuple 
def sports_ranking(team:str, league:str, season:int=None):
	"""
	sports_ranking : Fetch the ranking of a specific sports team in a specific league    
	Parameters:
	team (str): The name of the team.
	league (str): The name of the league.
	season (int): Optional parameter to specify the season, default is the current season, 2024

	Required Parameter = [team,league,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def calculate_compound_interest(principle:float, interest_rate:float, time:int, compounds_per_year:int=None):
	"""
	calculate_compound_interest : Calculates the compound interest of an investment over a given time period.    
	Parameters:
	principle (float): The initial amount of the investment.
	interest_rate (float): The yearly interest rate of the investment.
	time (int): The time, in years, the money is invested or borrowed for.
	compounds_per_year (int): The number of times the interest is compounded per year. Default is 1 (interest is compounded yearly).

	Required Parameter = [principle,interest_rate,time,]

	"""
	pass

tools = [sports_ranking, calculate_compound_interest]
