from typing import List, Dict, Any, Union, Tuple, Set 
def payment_calculation(items:List[str], quantities:List[int]) -> str:
	"""
	payment_calculation : Calculate how much a person should pay given the items purchased and their quantities    
	Parameters:
	items (List[str]): List of items purchased.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	quantities (List[int]): Quantity of each item purchased in correspondence with the previous items list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [items,quantities,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def steps_calorie_calculation(calorie:float) -> str:
	"""
	steps_calorie_calculation : Calculate how many steps you need to walk to burn a specified amount of calories.    
	Parameters:
	calorie (float): The amount of calories to burn.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [calorie,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hydration_calculator(exercise_time:float) -> str:
	"""
	hydration_calculator : Calculate the amount of water to drink in a day given the hours of exercise.    
	Parameters:
	exercise_time (float): The number of hours of exercise.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [exercise_time,]

	"""
	return 'Success'

tools = [payment_calculation, steps_calorie_calculation, hydration_calculator]
