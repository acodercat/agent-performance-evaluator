from typing import List, Dict, Any, Union, Tuple, Set 
def get_earliest_reference(name:str, source:str=None) -> str:
	"""
	get_earliest_reference : Retrieve the earliest historical reference of a person.    
	Parameters:
	name (str): The name of the person.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	source (str): Source to fetch the reference. Default is 'scriptures'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_current_time(city:str, country:str, format:str=None) -> str:
	"""
	get_current_time : Retrieve the current time for a specified city and country.    
	Parameters:
	city (str): The city for which the current time is to be retrieved.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	country (str): The country where the city is located.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	format (str): The format in which the time is to be displayed, optional (defaults to 'HH:MM:SS').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [city,country,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def music_generator_generate_melody(key:str, start_note:str, length:int, tempo:int=None) -> str:
	"""
	music_generator_generate_melody : Generate a melody based on certain musical parameters.    
	Parameters:
	key (str): The key of the melody. E.g., 'C' for C major.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	start_note (str): The first note of the melody, specified in scientific pitch notation. E.g., 'C4'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	length (int): The number of measures in the melody.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	tempo (int): The tempo of the melody, in beats per minute. Optional parameter. If not specified, defaults to 120.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [key,start_note,length,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def geometry_circumference(radius:int, units:str=None) -> str:
	"""
	geometry_circumference : Calculate the circumference of a circle given the radius.    
	Parameters:
	radius (int): The radius of the circle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	units (str): Units for the output circumference measurement. Default is 'cm'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [radius,]

	"""
	return 'Success'

tools = [get_earliest_reference, get_current_time, music_generator_generate_melody, geometry_circumference]
