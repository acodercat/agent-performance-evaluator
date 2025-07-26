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
def mix_paint_color(color1:str, color2:str, lightness:int=None) -> str:
	"""
	mix_paint_color : Combine two primary paint colors and adjust the resulting color's lightness level.    
	Parameters:
	color1 (str): The first primary color to be mixed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	color2 (str): The second primary color to be mixed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	lightness (int): The desired lightness level of the resulting color in percentage. The default level is set to 50%.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [color1,color2,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def finance_calculate_quarterly_dividend_per_share(total_payout:int, outstanding_shares:int) -> str:
	"""
	finance_calculate_quarterly_dividend_per_share : Calculate quarterly dividend per share for a company given total dividend payout and outstanding shares    
	Parameters:
	total_payout (int): The total amount of dividends paid out in USD
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	outstanding_shares (int): Total number of outstanding shares
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [total_payout,outstanding_shares,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def movie_details_brief(title:str, extra_info:bool='false') -> str:
	"""
	movie_details_brief : This function retrieves a brief about a specified movie.    
	Parameters:
	title (str): Title of the movie
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	extra_info (bool): Option to get additional information like Director, Cast, Awards etc.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [title,]

	"""
	return 'Success'

tools = [get_song_lyrics, mix_paint_color, finance_calculate_quarterly_dividend_per_share, movie_details_brief]
