from typing import List, Dict, Any, Union, Tuple, Set 
def concert_book_ticket(artist:str, location:str, add_ons:List[str]=None) -> str:
	"""
	concert_book_ticket : Book a ticket for a concert at a specific location with various add-ons like backstage pass.    
	Parameters:
	artist (str): Name of the artist for the concert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): City where the concert will take place.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	add_ons (List[str]): Add-ons for the concert. Default is 'VIP Seating' if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [artist,location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def festival_book_ticket(festival:str, location:str, add_ons:List[str]=None) -> str:
	"""
	festival_book_ticket : Book a ticket for a festival at a specific location with various add-ons like camping access.    
	Parameters:
	festival (str): Name of the festival.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): City where the festival will take place.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	add_ons (List[str]): Add-ons for the festival. Default is 'Camping Pass' if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [festival,location,]

	"""
	return 'Success'

tools = [concert_book_ticket, festival_book_ticket]
