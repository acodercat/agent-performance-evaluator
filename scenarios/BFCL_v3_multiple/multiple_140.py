from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuits_search(company_name:str, location:str, year:int, case_type:str=None) -> str:
	"""
	lawsuits_search : Search for lawsuits against a specific company within a specific time and location.    
	Parameters:
	company_name (str): The name of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location where the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year when the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	case_type (str): The type of the case. Options include: 'civil', 'criminal', 'small_claims', etc. If not specified, search for all types. Default is 'all'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,location,year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hilton_hotel_check_availability(location:str, check_in_date:str, check_out_date:str, no_of_adults:int, hotel_chain:str='Hilton') -> str:
	"""
	hilton_hotel_check_availability : Check hotel availability for a specific location and time frame.    
	Parameters:
	location (str): The city where you want to check hotel availability.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	check_in_date (str): The check-in date in the format YYYY-MM-DD.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	check_out_date (str): The check-out date in the format YYYY-MM-DD.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	no_of_adults (int): The number of adults for the hotel booking.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	hotel_chain (str): The hotel chain where you want to book the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,check_in_date,check_out_date,no_of_adults,]

	"""
	return 'Success'

tools = [lawsuits_search, hilton_hotel_check_availability]
