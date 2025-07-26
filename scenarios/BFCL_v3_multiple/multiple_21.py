from typing import List, Dict, Any, Union, Tuple, Set 
def play_sound_wave(wave_file:str, volume:float=1) -> str:
	"""
	play_sound_wave : This function is for playing a sound wave file.    
	Parameters:
	wave_file (str): The filename of the sound wave file to be played.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	volume (float): The volume level at which the sound is to be played (1 is 100%).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [wave_file,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def generate_sound_wave(frequency:int, duration:int, wave_type:str='sine') -> str:
	"""
	generate_sound_wave : This function is for generating a sinusoidal sound wave file of a certain frequency for a specific duration and save it to a WAV file.    
	Parameters:
	frequency (int): The frequency of the sound wave in Hz.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (int): The duration of the sound in seconds.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	wave_type (str): The waveform to be used to generate the sound.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [frequency,duration,]

	"""
	return 'Success'

tools = [play_sound_wave, generate_sound_wave]
