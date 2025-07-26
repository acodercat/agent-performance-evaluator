from typing import List, Dict, Any, Union, Tuple, Set 
def get_scientist_for_discovery(discovery:str) -> str:
	"""
	get_scientist_for_discovery : Retrieve the scientist's name who is credited for a specific scientific discovery or theory.    
	Parameters:
	discovery (str): The scientific discovery or theory.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [discovery,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def game_stats_fetch_player_statistics(game:str, username:str, platform:str='PC') -> str:
	"""
	game_stats_fetch_player_statistics : Fetch player statistics for a specific video game for a given user.    
	Parameters:
	game (str): The name of the video game.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	username (str): The username of the player.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	platform (str): The platform user is playing on.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [game,username,]

	"""
	return 'Success'

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
	time (str): Preferred time of flight. Default to none if not provided. Accepts standard time format e.g., 10:00 AM
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	direct_flight (bool): If set to true, only direct flights will be searched. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [departure_location,destination_location,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def event_finder_find_upcoming(location:str, genre:str, days_ahead:int=7) -> str:
	"""
	event_finder_find_upcoming : Find upcoming events of a specific genre in a given location.    
	Parameters:
	location (str): The city and state where the search will take place, e.g. New York, NY.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	genre (str): The genre of events.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days_ahead (int): The number of days from now to include in the search.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,genre,]

	"""
	return 'Success'

tools = [get_scientist_for_discovery, game_stats_fetch_player_statistics, flight_book, event_finder_find_upcoming]
