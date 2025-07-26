from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_details_find(company_name:str, year:int, case_type:str=None) -> str:
	"""
	lawsuit_details_find : Find details of lawsuits involving a specific company from a given year.    
	Parameters:
	company_name (str): Name of the company.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year of the lawsuit.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	case_type (str): Type of the lawsuit, e.g., 'IPR', 'Patent', 'Commercial', etc. Default is 'all'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company_name,year,]

	"""
	return 'Success'

tools = [lawsuit_details_find]
