from typing import List, Dict, Any, Union, Tuple, Set 
def law_case_search(topic:str, year_range:List[int], location:str, judicial_system:str='all') -> str:
	"""
	law_case_search : Search and retrieve law cases based on the topic, timeline, and location.    
	Parameters:
	topic (str): The subject matter of the case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year_range (List[int]): The start and end year for searching cases.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The location where the case is being heard.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	judicial_system (str): The specific judicial system in which to search (e.g. 'federal', 'state').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [topic,year_range,location,]

	"""
	return 'Success'

tools = [law_case_search]
