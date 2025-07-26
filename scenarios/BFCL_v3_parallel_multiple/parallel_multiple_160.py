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
	case_type (str): The type of the case. Options include: 'civil', 'criminal', 'small_claims', etc. If not specified, default to search for all types.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,location,year,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def compound_interest(principal:int, annual_rate:float, compounding_freq:str, time_in_years:int) -> str:
	"""
	compound_interest : Calculate compound interest for a certain time period.    
	Parameters:
	principal (int): The initial amount of money that was invested or loaned out.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	annual_rate (float): The interest rate for a year as a percentage.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	compounding_freq (str): The number of times that interest is compounded per unit period.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time_in_years (int): The time the money is invested for in years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principal,annual_rate,compounding_freq,time_in_years,]

	"""
	return 'Success'

tools = [lawsuits_search, compound_interest]
