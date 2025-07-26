from typing import List, Dict, Any, Union, Tuple, Set 
def concert_booking_book_ticket(artist:str, city:str, num_tickets:int=None) -> str:
	"""
	concert_booking_book_ticket : Book concert tickets for a specific artist in a specified city.    
	Parameters:
	artist (str): The artist you want to book tickets for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city where the concert is.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	num_tickets (int): Number of tickets required. Default is 1.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [artist,city,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_magnetic_field(current:int, radius:int, permeability:float=None) -> str:
	"""
	calculate_magnetic_field : Calculate the magnetic field produced at the center of a circular loop carrying current.    
	Parameters:
	current (int): The current through the circular loop in Amperes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	radius (int): The radius of the circular loop in meters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	permeability (float): The magnetic permeability. Default is permeability in free space, 0.01
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [current,radius,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_details_find(company_name:str, year:int, case_type:str=None) -> str:
	"""
	lawsuit_details_find : Find details of lawsuits involving a specific company from a given year.    
	Parameters:
	company_name (str): Name of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year of the lawsuit.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	case_type (str): Type of the lawsuit, e.g., 'IPR', 'Patent', 'Commercial', etc. This is an optional parameter. Default is 'all'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,year,]

	"""
	return 'Success'

tools = [concert_booking_book_ticket, calculate_magnetic_field, lawsuit_details_find]
