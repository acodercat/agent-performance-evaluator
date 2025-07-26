from typing import List, Dict, Any, Union, Tuple, Set 
def get_stock_price(company_names:List[str]) -> str:
	"""
	get_stock_price : Retrieves the current stock price of the specified companies    
	Parameters:
	company_names (List[str]): The list of companies for which to retrieve the stock price.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_names,]

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
def park_information(park_name:str, information:List[str]) -> str:
	"""
	park_information : Retrieve the basic information such as elevation and area of a national park.    
	Parameters:
	park_name (str): The name of the national park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	information (List[str]): The type of information you want about the park.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [park_name,information,]

	"""
	return 'Success'

tools = [get_stock_price, get_song_lyrics, park_information]
