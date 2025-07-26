from typing import List, Dict, Any, Union, Tuple, Set 
def euro_history_treaty_info(treaty_name:str, info_requested:List[str]) -> str:
	"""
	euro_history_treaty_info : Retrieve specific information about a signed European treaty.    
	Parameters:
	treaty_name (str): The name of the treaty.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	info_requested (List[str]): Specific aspects of the treaty for which to return information.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [treaty_name,info_requested,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def euro_history_battle_details(battle_name:str, specific_info:List[str]) -> str:
	"""
	euro_history_battle_details : Retrieve detailed information about a specific European historical battle.    
	Parameters:
	battle_name (str): The name of the historical battle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	specific_info (List[str]): The specific types of information to return about the battle.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [battle_name,specific_info,]

	"""
	return 'Success'

tools = [euro_history_treaty_info, euro_history_battle_details]
