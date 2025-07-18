from typing import List, Dict, Any, Union, Tuple 
def sports_ranking_get_current(team:str, league:str, season:str=None):
	"""
	sports_ranking_get_current : Retrieve the current ranking of a specific team in a particular league.    
	Parameters:
	team (str): The name of the team whose ranking is sought.
	league (str): The league in which the team participates.
	season (str): The season for which the ranking is sought. Defaults to the current season if not provided.

	Required Parameter = [team,league,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def get_earliest_reference(name:str, source:str=None):
	"""
	get_earliest_reference : Retrieve the earliest historical reference of a person.    
	Parameters:
	name (str): The name of the person.
	source (str): Source to fetch the reference. Default is 'scriptures'

	Required Parameter = [name,]

	"""
	pass

tools = [sports_ranking_get_current, get_earliest_reference]
