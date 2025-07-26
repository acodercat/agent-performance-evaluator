from typing import List, Dict, Any, Union, Tuple, Set 
def music_generator_generate_scale_progression(key:str, tempo:int, duration:int, scale_type:str='major') -> str:
	"""
	music_generator_generate_scale_progression : Generate a music scale progression in a specific key with a given tempo and duration.    
	Parameters:
	key (str): The key in which to generate the scale progression.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	tempo (int): The tempo of the scale progression in BPM.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (int): The duration of each note in beats.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	scale_type (str): The type of scale to generate. Defaults to 'major'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [key,tempo,duration,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def math_hcf(number1:int, number2:int) -> str:
	"""
	math_hcf : Calculate the highest common factor of two numbers.    
	Parameters:
	number1 (int): First number.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number2 (int): Second number.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number1,number2,]

	"""
	return 'Success'

tools = [music_generator_generate_scale_progression, math_hcf]
