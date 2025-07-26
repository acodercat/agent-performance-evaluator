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

tools = [music_generator_generate_melody]
