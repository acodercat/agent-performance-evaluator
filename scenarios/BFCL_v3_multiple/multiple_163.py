def metropolitan_museum_get_top_artworks(number, sort_by=None):
	"""
	Fetches the list of popular artworks at the Metropolitan Museum of Art. Results can be sorted based on popularity.    
	Parameters:
	number: The number of artworks to fetch
	sort_by: The criteria to sort the results on. Default is ''.

	"""
	pass

def lawsuit_search(company, start_date, location, status=None):
	"""
	Search for lawsuits related to a specific company within a specific date range and location.    
	Parameters:
	company: The company related to the lawsuit.
	start_date: Start of the date range for when the lawsuit was filed.
	location: Location where the lawsuit was filed.
	status: The status of the lawsuit. Default is 'ongoing'.

	"""
	pass

tools = [metropolitan_museum_get_top_artworks, lawsuit_search]
