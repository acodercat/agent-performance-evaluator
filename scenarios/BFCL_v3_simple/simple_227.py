from typing import List, Dict, Any, Union, Tuple, Set 
def get_personality_traits(type:str, traits:List[str]=None) -> str:
	"""
	get_personality_traits : Retrieve the personality traits for a specific personality type, including their strengths and weaknesses.    
	Parameters:
	type (str): The personality type.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	traits (List[str]): List of traits to be retrieved, default is ['strengths'].
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [type,]

	"""
	return 'Success'

tools = [get_personality_traits]
