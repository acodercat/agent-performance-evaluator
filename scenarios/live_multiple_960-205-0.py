def get_current_weather(location, unit='fahrenheit'):
	"""
	Retrieves the current weather conditions for a specified location.    
	Parameters:
	location: The city and state for which to get the weather, in the format of 'City, State', such as 'San Francisco, CA' or 'New York, NY'.
	unit: The unit of measurement for temperature values.

	"""
	pass

def web_search(query, results_limit=10, language='en', safe_search=True):
	"""
	Perform a web search for a given query and return relevant results.    
	Parameters:
	query: The search query string to be used for finding relevant web pages.
	results_limit: The maximum number of search results to return. The value must be a positive integer.
	language: The language preference for the search results.
	safe_search: Enable or disable safe search filtering.

	"""
	pass

tools = [get_current_weather, web_search]
