from typing import List, Dict, Any, Union, Tuple, Set 
def sports_ranking(team:str, league:str, season:int=None):
	"""
	sports_ranking : Fetch the ranking of a specific sports team in a specific league    
	Parameters:
	team (str): The name of the team.
	league (str): The name of the league.
	season (int): Optional parameter to specify the season, default is the current season.

	Required Parameter = [team,league,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def air_quality(location:str, date:str):
	"""
	air_quality : Retrieve the air quality index for a specific location.    
	Parameters:
	location (str): The city that you want to get the air quality index for.
	date (str): The date you want to get the air quality index for. Default is today.

	Required Parameter = [location,date,]

	"""
	pass

tools = [sports_ranking, air_quality]
