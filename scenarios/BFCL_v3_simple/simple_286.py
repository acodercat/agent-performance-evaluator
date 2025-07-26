from typing import List, Dict, Any, Union, Tuple, Set 
def concert_get_details(artist:str, location:str, date:str=None) -> str:
	"""
	concert_get_details : Fetch the details for a particular concert based on the artist and location.    
	Parameters:
	artist (str): Name of the artist/band who's performing.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): City where the concert is taking place.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): Date of the concert in 'mm-yyyy' format. Default is the current month if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [artist,location,]

	"""
	return 'Success'

tools = [concert_get_details]
