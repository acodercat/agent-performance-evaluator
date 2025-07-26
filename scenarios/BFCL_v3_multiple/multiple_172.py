from typing import List, Dict, Any, Union, Tuple, Set 
def get_traffic_info(start_location:str, end_location:str, mode:str=None) -> str:
	"""
	get_traffic_info : Retrieve current traffic conditions for a specified route.    
	Parameters:
	start_location (str): The starting point of the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end_location (str): The destination of the route.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mode (str): Preferred method of transportation, default to 'driving'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [start_location,end_location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_compound_interest(principle:float, interest_rate:float, time:int, compounds_per_year:int=None) -> str:
	"""
	calculate_compound_interest : Calculates the compound interest of an investment over a given time period.    
	Parameters:
	principle (float): The initial amount of the investment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	interest_rate (float): The yearly interest rate of the investment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The time, in years, the money is invested or borrowed for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	compounds_per_year (int): The number of times the interest is compounded per year. Default is 1 (interest is compounded yearly).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle,interest_rate,time,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def cooking_conversion_convert(quantity:int, from_unit:str, to_unit:str, item:str) -> str:
	"""
	cooking_conversion_convert : Convert cooking measurements from one unit to another.    
	Parameters:
	quantity (int): The quantity to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	from_unit (str): The unit to convert from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_unit (str): The unit to convert to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	item (str): The item to be converted.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [quantity,from_unit,to_unit,item,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sports_db_find_athlete(name:str, sport:str, team:str=None) -> str:
	"""
	sports_db_find_athlete : Find the profile information of a sports athlete based on their full name.    
	Parameters:
	name (str): The full name of the athlete.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team (str): The team the athlete belong to. Default is ''
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	sport (str): The sport that athlete plays.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [name,sport,]

	"""
	return 'Success'

tools = [get_traffic_info, calculate_compound_interest, cooking_conversion_convert, sports_db_find_athlete]
