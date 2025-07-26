from typing import List, Dict, Any, Union, Tuple, Set 
def physics_wave_velocity(frequency:float, wavelength:float) -> str:
	"""
	physics_wave_velocity : Calculate the velocity of a wave based on its frequency and wavelength.    
	Parameters:
	frequency (float): The frequency of the wave in Hz.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	wavelength (float): The wavelength of the wave in m.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [frequency,wavelength,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def kinematics_final_velocity(initial_velocity:int, time:int, acceleration:float=None) -> str:
	"""
	kinematics_final_velocity : Find the final velocity of an object moving under constant acceleration.    
	Parameters:
	initial_velocity (int): The initial velocity of the object in m/s.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The time in seconds the object has been moving.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	acceleration (float): The acceleration of the object in m/s^2. Default value is -9.81 (Earth's gravity)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [initial_velocity,time,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def kinematics_distance(initial_velocity:float, time:int, acceleration:float=None) -> str:
	"""
	kinematics_distance : Find the distance traveled by an object moving under constant acceleration.    
	Parameters:
	initial_velocity (float): The initial velocity of the object in m/s.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The time in seconds the object has been moving.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	acceleration (float): The acceleration of the object in m/s^2. Default value is -9.81 (Earth's gravity)
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [initial_velocity,time,]

	"""
	return 'Success'

tools = [physics_wave_velocity, kinematics_final_velocity, kinematics_distance]
