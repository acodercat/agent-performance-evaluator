from typing import List, Dict, Any, Union, Tuple, Set 
def concert_book_ticket(artist:str, location:str, add_ons:List[str]=None):
	"""
	concert_book_ticket : Book a ticket for a concert at a specific location with various add-ons like backstage pass.    
	Parameters:
	artist (str): Name of the artist for the concert.
	location (str): City where the concert will take place.
	add_ons (List[str]): Add-ons for the concert. Default is 'VIP Seating' if not specified.

	Required Parameter = [artist,location,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def festival_book_ticket(festival:str, location:str, add_ons:List[str]=None):
	"""
	festival_book_ticket : Book a ticket for a festival at a specific location with various add-ons like camping access.    
	Parameters:
	festival (str): Name of the festival.
	location (str): City where the festival will take place.
	add_ons (List[str]): Add-ons for the festival. Default is 'Camping Pass' if not specified.

	Required Parameter = [festival,location,]

	"""
	pass

tools = [concert_book_ticket, festival_book_ticket]
