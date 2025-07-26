from typing import List, Dict, Any, Union, Tuple, Set 
def get_news(topic:str, quantity:int, region:str=None) -> str:
	"""
	get_news : Fetches the latest news on a specific topic.    
	Parameters:
	topic (str): The subject for the news topic.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	quantity (int): Number of articles to fetch.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	region (str): The geographical region for the news (Optional). default is 'USA'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [topic,quantity,]

	"""
	return 'Success'

tools = [get_news]
