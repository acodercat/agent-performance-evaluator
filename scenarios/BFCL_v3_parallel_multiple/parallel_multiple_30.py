from typing import List, Dict, Any, Union, Tuple, Set 
def movie_ratings_get_movie(movie_name:str) -> str:
	"""
	movie_ratings_get_movie : Get a movie by its name.    
	Parameters:
	movie_name (str): The name of the movie to be retrieved
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [movie_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def legal_case_get_summary(case_id:str, summary_type:str='brief') -> str:
	"""
	legal_case_get_summary : Get a summary of a legal case    
	Parameters:
	case_id (str): The unique ID of the case to summarise
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	summary_type (str): Type of the summary to get, e.g., brief, full
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_id,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def legal_case_find_parties(party_name:str, city:str) -> str:
	"""
	legal_case_find_parties : Locate legal cases involving a specified party in a particular city    
	Parameters:
	party_name (str): The name of the party involved in the case
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city where the case was heard
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [party_name,city,]

	"""
	return 'Success'

tools = [movie_ratings_get_movie, legal_case_get_summary, legal_case_find_parties]
