from typing import List, Dict, Any, Union, Tuple, Set 
def history_fact_fetch(event:str, depth:str='detailed', year:int=None) -> str:
	"""
	history_fact_fetch : Retrieve facts about historical events or documents    
	Parameters:
	event (str): The historical event or document you want to know about.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	depth (str): The depth of information required. Choices are 'brief' or 'detailed'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): The year of the event/document. default is 0
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [event,]

	"""
	return 'Success'

tools = [history_fact_fetch]
