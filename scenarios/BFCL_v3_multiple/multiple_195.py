from typing import List, Dict, Any, Union, Tuple, Set 
def get_lawsuit_details(case_number:str, court_location:str, additional_details:List[str]=None) -> str:
	"""
	get_lawsuit_details : Retrieve the detailed information about a lawsuit based on its case number and the court location.    
	Parameters:
	case_number (str): The case number of the lawsuit.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	court_location (str): The location of the court where the case is filed.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	additional_details (List[str]): Optional. Array containing additional details to be fetched. Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [case_number,court_location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_team_rank(team_name:str, league:str, season:str, type:str) -> str:
	"""
	get_team_rank : Get the team ranking in a sports league based on season and type.    
	Parameters:
	team_name (str): The name of the sports team.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	league (str): The name of the league in which the team competes.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	season (str): The season for which the team's ranking is sought.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Type of the season: regular or playoff.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [team_name,league,season,type,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calc_heat_capacity(temp:int, volume:int, gas:str=None) -> str:
	"""
	calc_heat_capacity : Calculate the heat capacity at constant pressure of air using its temperature and volume.    
	Parameters:
	temp (int): The temperature of the gas in Kelvin.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	volume (int): The volume of the gas in m^3.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	gas (str): Type of gas, with air as default.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [temp,volume,]

	"""
	return 'Success'

tools = [get_lawsuit_details, get_team_rank, calc_heat_capacity]
