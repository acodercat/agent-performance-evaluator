from typing import List, Dict, Any, Union, Tuple, Set 
def flight_book(departure_location:str, destination_location:str, date:str, time:str=None, direct_flight:bool=None) -> str:
	"""
	flight_book : Book a direct flight for a specific date and time from departure location to destination location.    
	Parameters:
	departure_location (str): The location you are departing from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination_location (str): The location you are flying to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date of the flight. Accepts standard date format e.g., 2022-04-28.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (str): Preferred time of flight. Default is 'anytime'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	direct_flight (bool): If set to true, only direct flights will be searched. Default is false
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [departure_location,destination_location,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuits_search(company_name:str, location:str, year:int, case_type:str=None) -> str:
	"""
	lawsuits_search : Search for lawsuits against a specific company within a specific time and location.    
	Parameters:
	company_name (str): The name of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location where the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year when the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	case_type (str): The type of the case. Options include: 'civil', 'criminal', 'small_claims', etc. If not specified, search for 'all' types by default.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,location,year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def imdb_find_movies_by_actor(actor_name:str, year:int, category:str=None) -> str:
	"""
	imdb_find_movies_by_actor : Searches the database to find all movies by a specific actor within a certain year.    
	Parameters:
	actor_name (str): The name of the actor.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The specific year to search in.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	category (str): The category of the film (e.g. Drama, Comedy, etc). This parameter is optional. Default is 'all'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [actor_name,year,]

	"""
	return 'Success'

tools = [flight_book, lawsuits_search, imdb_find_movies_by_actor]
