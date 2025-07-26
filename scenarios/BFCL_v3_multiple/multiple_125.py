from typing import List, Dict, Any, Union, Tuple, Set 
def restaurant_search_find_closest(location:str, cuisine:str, amenities:List[str]=None) -> str:
	"""
	restaurant_search_find_closest : Locate the closest sushi restaurant based on certain criteria, such as the presence of a patio.    
	Parameters:
	location (str): The city, for instance Boston, MA
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cuisine (str): Type of food like Sushi.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amenities (List[str]): Preferred amenities in the restaurant. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,cuisine,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def run_two_sample_ttest(group1:List[int], group2:List[int], equal_variance:bool=True) -> str:
	"""
	run_two_sample_ttest : Runs a two sample t-test for two given data groups.    
	Parameters:
	group1 (List[int]): First group of data points.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	group2 (List[int]): Second group of data points.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	equal_variance (bool): Assumption about whether the two samples have equal variance.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [group1,group2,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_personality_traits(hobby:str, trait_count:int=None) -> str:
	"""
	get_personality_traits : Retrieve the common personality traits of people based on their hobbies or activities.    
	Parameters:
	hobby (str): The hobby or activity of interest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	trait_count (int): The number of top traits to return, default is 5
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [hobby,]

	"""
	return 'Success'

tools = [restaurant_search_find_closest, run_two_sample_ttest, get_personality_traits]
