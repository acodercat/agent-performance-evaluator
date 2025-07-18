from typing import List, Dict, Any, Union, Tuple 
def get_current_time(location:str):
	"""
	get_current_time : Fetches current time for a given location    
	Parameters:
	location (str): The location for which to fetch current time

	Required Parameter = [location,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def translate_text(text:str, from_lang:str, to_lang:str):
	"""
	translate_text : Translates a given text from one language to another    
	Parameters:
	text (str): The text that needs to be translated
	from_lang (str): The source language from which to translate
	to_lang (str): The target language to which to translate

	Required Parameter = [text,from_lang,to_lang,]

	"""
	pass

tools = [get_current_time, translate_text]
