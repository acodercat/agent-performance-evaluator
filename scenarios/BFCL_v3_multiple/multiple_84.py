from typing import List, Dict, Any, Union, Tuple, Set 
def getTopGoalScorers(competition:str, team:str, number:int) -> str:
	"""
	getTopGoalScorers : Returns the top goal scorers for a specific competition and team    
	Parameters:
	competition (str): The name of the competition (for example, 'UEFA Champions League').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team (str): The name of the team (for example, 'Barcelona').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number (int): The number of top goal scorers to retrieve.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [competition,team,number,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def getTopAssists(competition:str, team:str, number:int) -> str:
	"""
	getTopAssists : Returns the top assist makers for a specific competition and team    
	Parameters:
	competition (str): The name of the competition (for example, 'UEFA Champions League').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	team (str): The name of the team (for example, 'Barcelona').
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	number (int): The number of top assist makers to retrieve.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [competition,team,number,]

	"""
	return 'Success'

tools = [getTopGoalScorers, getTopAssists]
