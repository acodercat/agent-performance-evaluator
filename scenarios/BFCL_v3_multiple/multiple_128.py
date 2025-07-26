from typing import List, Dict, Any, Union, Tuple, Set 
def public_library_find_nearby(location:str, facilities:List[str]) -> str:
	"""
	public_library_find_nearby : Locate nearby public libraries based on specific criteria like English fiction availability and Wi-Fi.    
	Parameters:
	location (str): The city and state, e.g. Boston, MA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	facilities (List[str]): Facilities and sections in public library.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,facilities,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_song_lyrics(song_title:str, artist_name:str, lang:str=None) -> str:
	"""
	get_song_lyrics : Retrieve the lyrics of a song based on the artist's name and song title.    
	Parameters:
	song_title (str): The title of the song.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	artist_name (str): The name of the artist who performed the song.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	lang (str): The language of the lyrics. Default is English.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [song_title,artist_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def law_case_search_find_historical(subject:str, from_year:int, to_year:int) -> str:
	"""
	law_case_search_find_historical : Search for a historical law case based on specific criteria like the subject and year.    
	Parameters:
	subject (str): The subject matter of the case, e.g., 'fraud'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_year (int): The start year for the range of the case. The case should happen after this year.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_year (int): The end year for the range of the case. The case should happen before this year.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [subject,from_year,to_year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_return_on_equity(net_income:int, shareholder_equity:int, dividends_paid:int=None) -> str:
	"""
	calculate_return_on_equity : Calculate a company's return on equity based on its net income, shareholder's equity, and dividends paid.    
	Parameters:
	net_income (int): The company's net income.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	shareholder_equity (int): The company's total shareholder's equity.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dividends_paid (int): The total dividends paid by the company. Optional. If not given, default it's 0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [net_income,shareholder_equity,]

	"""
	return 'Success'

tools = [public_library_find_nearby, get_song_lyrics, law_case_search_find_historical, calculate_return_on_equity]
