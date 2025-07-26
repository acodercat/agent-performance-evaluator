from typing import List, Dict, Any, Union, Tuple, Set 
def briefs_display_cases(case_id:List[str]) -> str:
	"""
	briefs_display_cases : Display briefs of the cases    
	Parameters:
	case_id (List[str]): A list of unique identifiers for cases.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_id,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def court_records_search_cases(location:str, query:str, year:int, limit:int=5) -> str:
	"""
	court_records_search_cases : Search for court cases based on specific criteria.    
	Parameters:
	location (str): The city where the court is located
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	query (str): Search string to look for specific cases
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year the case was filed
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	limit (int): Limits the number of results returned
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,query,year,]

	"""
	return 'Success'

tools = [briefs_display_cases, court_records_search_cases]
