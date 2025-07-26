from typing import List, Dict, Any, Union, Tuple, Set 
def religion_history_info(religion:str, till_century:int, include_people:bool=None) -> str:
	"""
	religion_history_info : Provides comprehensive historical details about a specified religion till a specified century.    
	Parameters:
	religion (str): The name of the religion for which historical details are needed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	till_century (int): The century till which historical details are needed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_people (bool): To include influential people related to the religion during that time period, default is False
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [religion,till_century,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def team_score_get_latest(team:str, include_opponent:bool='false') -> str:
	"""
	team_score_get_latest : Retrieve the score of the most recent game for a specified sports team.    
	Parameters:
	team (str): Name of the sports team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	include_opponent (bool): Include the name of the opponent team in the return.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def concert_search(genre:str, location:str, date:str, price_range:str=None) -> str:
	"""
	concert_search : Locate a concert based on specific criteria like genre, location, and date.    
	Parameters:
	genre (str): Genre of the concert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): City of the concert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): Date of the concert, e.g. this weekend, today, tomorrow, or date string.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	price_range (str): Expected price range of the concert tickets. Default is 'any'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [genre,location,date,]

	"""
	return 'Success'

tools = [religion_history_info, team_score_get_latest, concert_search]
