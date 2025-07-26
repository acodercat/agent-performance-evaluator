from typing import List, Dict, Any, Union, Tuple, Set 
def music_generate(key:str, tempo:int, time_signature:str=None) -> str:
	"""
	music_generate : Generate a piece of music given a key, tempo, and time signature.    
	Parameters:
	key (str): The key of the piece, e.g., C Major.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	tempo (int): Tempo of the piece in beats per minute.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time_signature (str): Time signature of the piece, e.g., 4/4. Default '4/4'
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [key,tempo,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def audio_generate(frequency:float, amplitude:float, duration:int=None) -> str:
	"""
	audio_generate : Generate an audio signal given a frequency, amplitude, and duration.    
	Parameters:
	frequency (float): Frequency of the audio signal in Hz.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amplitude (float): Amplitude of the audio signal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (int): Duration of the audio signal in seconds. Default 1
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [frequency,amplitude,]

	"""
	return 'Success'

tools = [music_generate, audio_generate]
