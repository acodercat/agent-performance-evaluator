def get_song_lyrics(song_title, artist_name, lang=None):
	"""
	Retrieve the lyrics of a song based on the artist's name and song title.    
	Parameters:
	song_title: The title of the song.
	artist_name: The name of the artist who performed the song.
	lang: The language of the lyrics. Default is English.

	"""
	pass

def law_case_search_find_historical(subject, from_year, to_year):
	"""
	Search for a historical law case based on specific criteria like the subject and year.    
	Parameters:
	subject: The subject matter of the case, e.g., 'fraud'
	from_year: The start year for the range of the case. The case should happen after this year.
	to_year: The end year for the range of the case. The case should happen before this year.

	"""
	pass

def calculate_return_on_equity(net_income, shareholder_equity, dividends_paid=None):
	"""
	Calculate a company's return on equity based on its net income, shareholder's equity, and dividends paid.    
	Parameters:
	net_income: The company's net income.
	shareholder_equity: The company's total shareholder's equity.
	dividends_paid: The total dividends paid by the company. Optional. If not given, default to 0.

	"""
	pass

def public_library_find_nearby(location, facilities):
	"""
	Locate nearby public libraries based on specific criteria like English fiction availability and Wi-Fi.    
	Parameters:
	location: The city and state, e.g. Boston, MA
	facilities: Facilities and sections in public library.

	"""
	pass

tools = [get_song_lyrics, law_case_search_find_historical, calculate_return_on_equity, public_library_find_nearby]
