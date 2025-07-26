from typing import List, Dict, Any, Union, Tuple, Set 
def train_ticket_buy(origin:str, destination:str, date:str) -> str:
	"""
	train_ticket_buy : Buy a train ticket for a specific date and route.    
	Parameters:
	origin (str): The departure full name of the city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	destination (str): The destination city.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): The date when the journey should be, in the format of yyyy-mm-dd.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [origin,destination,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def musical_ticket_buy(show:str, date:str) -> str:
	"""
	musical_ticket_buy : Buy a ticket for a musical    
	Parameters:
	show (str): Name of the show.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): Date when the ticket should be bought for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [show,date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def concert_ticket_buy(artist:str, date:str) -> str:
	"""
	concert_ticket_buy : Buy a concert ticket    
	Parameters:
	artist (str): Name of the artist.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	date (str): Date of the concert.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [artist,date,]

	"""
	return 'Success'

tools = [train_ticket_buy, musical_ticket_buy, concert_ticket_buy]
