from typing import List, Dict, Any, Union, Tuple, Set 
def discoverer_get(element_name:str, year:int=None, first:bool=True) -> str:
	"""
	discoverer_get : Retrieve the name of the discoverer of an element based on its name.    
	Parameters:
	element_name (str): The name of the element.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Optional parameter that refers to the year of discovery. It could be helpful in case an element was discovered more than once. Default is 0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	first (bool): Optional parameter indicating if the first discoverer's name should be retrieved.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [element_name,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def lawsuit_check_case(case_id:int, closed_status:bool) -> str:
	"""
	lawsuit_check_case : Verify the details of a lawsuit case and check its status using case ID.    
	Parameters:
	case_id (int): The identification number of the lawsuit case.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	closed_status (bool): The status of the lawsuit case to be verified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_id,closed_status,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_museum_hours(museum_name:str, day:str) -> str:
	"""
	get_museum_hours : Retrieve opening hours of a specified museum for the specified day.    
	Parameters:
	museum_name (str): The name of the museum.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	day (str): Day of the week.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum_name,day,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def monopoly_odds_calculator(number:int, dice_number:int, dice_faces:int=None) -> str:
	"""
	monopoly_odds_calculator : Calculates the probability of rolling a certain sum with two dice, commonly used in board game like Monopoly.    
	Parameters:
	number (int): The number for which the odds are calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dice_number (int): The number of dice involved in the roll.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dice_faces (int): The number of faces on a single die. Default is 6 for standard six-faced die.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [number,dice_number,]

	"""
	return 'Success'

tools = [discoverer_get, lawsuit_check_case, get_museum_hours, monopoly_odds_calculator]
