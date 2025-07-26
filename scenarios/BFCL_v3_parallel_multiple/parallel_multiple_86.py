from typing import List, Dict, Any, Union, Tuple, Set 
def kinematics_calculate_acceleration(initial_speed:float, final_speed:float, time:float, distance:float=0) -> str:
	"""
	kinematics_calculate_acceleration : Calculates the acceleration of an object under given conditions.    
	Parameters:
	initial_speed (float): The initial speed of the object.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	final_speed (float): The final speed of the object.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (float): The time in seconds it took the object to reach the final speed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	distance (float): The distance in meters the object has traveled.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [initial_speed,final_speed,time,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def kinematics_calculate_speed_from_rest(distance:float, time:float, initial_speed:float=0) -> str:
	"""
	kinematics_calculate_speed_from_rest : Calculates the speed of an object that starts from rest under a constant acceleration over a specified distance.    
	Parameters:
	distance (float): The distance in meters the object has traveled.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (float): The time in seconds it took the object to travel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	initial_speed (float): The initial speed of the object.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [distance,time,]

	"""
	return 'Success'

tools = [kinematics_calculate_acceleration, kinematics_calculate_speed_from_rest]
