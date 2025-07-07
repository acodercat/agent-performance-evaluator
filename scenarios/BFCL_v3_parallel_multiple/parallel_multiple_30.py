def movie_ratings_get_movie(movie_name):
	"""
	Get a movie by its name.    
	Parameters:
	movie_name: The name of the movie to be retrieved

	"""
	pass

def legal_case_get_summary(case_id, summary_type='brief'):
	"""
	Get a summary of a legal case    
	Parameters:
	case_id: The unique ID of the case to summarise
	summary_type: Type of the summary to get, e.g., brief, full

	"""
	pass

def legal_case_find_parties(party_name, city):
	"""
	Locate legal cases involving a specified party in a particular city    
	Parameters:
	party_name: The name of the party involved in the case
	city: The city where the case was heard

	"""
	pass

tools = [movie_ratings_get_movie, legal_case_get_summary, legal_case_find_parties]
