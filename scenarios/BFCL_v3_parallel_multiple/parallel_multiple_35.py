from typing import List, Dict, Any, Union, Tuple, Set 
def image_processing_object_identification(image_url:str) -> str:
	"""
	image_processing_object_identification : Identify objects in a given image.    
	Parameters:
	image_url (str): The URL of the image.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [image_url,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def text_analysis_sentiment_analysis(text:str) -> str:
	"""
	text_analysis_sentiment_analysis : Analyze the sentiment of a given text.    
	Parameters:
	text (str): The text to be analyzed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [text,]

	"""
	return 'Success'

tools = [image_processing_object_identification, text_analysis_sentiment_analysis]
