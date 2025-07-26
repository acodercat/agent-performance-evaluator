from typing import List, Dict, Any, Union, Tuple, Set 
def painting_create(shape:str, background_color:str, dimensions:List[int]) -> str:
	"""
	painting_create : Creates a new painting with specified parameters    
	Parameters:
	shape (str): Shape of the painting to be created.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	background_color (str): Background color of the painting.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dimensions (List[int]): Dimensions of the painting in inches.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [shape,background_color,dimensions,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def display_set_screen_brightness(percentage:int, duration:int) -> str:
	"""
	display_set_screen_brightness : Sets the screen brightness for viewing the painting    
	Parameters:
	percentage (int): Screen brightness level in percentage.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (int): Duration to maintain the brightness level in seconds.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [percentage,duration,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def painting_display(time:int) -> str:
	"""
	painting_display : Displays a created painting for a specific amount of time    
	Parameters:
	time (int): Time in seconds the painting will be displayed for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [time,]

	"""
	return 'Success'

tools = [painting_create, display_set_screen_brightness, painting_display]
