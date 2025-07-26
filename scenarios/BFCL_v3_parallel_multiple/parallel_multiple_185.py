from typing import List, Dict, Any, Union, Tuple, Set 
def metropolitan_museum_get_top_artworks(number:int, sort_by:str=None) -> str:
	"""
	metropolitan_museum_get_top_artworks : Fetches the list of popular artworks at the Metropolitan Museum of Art. Results can be sorted based on popularity.    
	Parameters:
	number (int): The number of artworks to fetch
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	sort_by (str): The criteria to sort the results on. Default is 'popularity'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_search(company:str, start_date:str, location:str, status:str=None) -> str:
	"""
	lawsuit_search : Search for lawsuits related to a specific company within a specific date range and location.    
	Parameters:
	company (str): The company related to the lawsuit.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	start_date (str): Start of the date range for when the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): Location where the lawsuit was filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	status (str): The status of the lawsuit. Default is 'ongoing'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,start_date,location,]

	"""
	return 'Success'

tools = [metropolitan_museum_get_top_artworks, lawsuit_search]
