from typing import List, Dict, Any, Union, Tuple 
def lawsuit_fetch_details(company_name:str):
	"""
	lawsuit_fetch_details : Fetch the details of a lawsuit for a specific company.    
	Parameters:
	company_name (str): The company involved in the lawsuit.

	Required Parameter = [company_name,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def lawsuit_judge(company_name:str, lawsuit_id:int=123):
	"""
	lawsuit_judge : Fetch the judge handling a lawsuit for a specific company.    
	Parameters:
	company_name (str): The company involved in the lawsuit.
	lawsuit_id (int): The ID number of the lawsuit. Default to 123

	Required Parameter = [company_name,]

	"""
	pass

tools = [lawsuit_fetch_details, lawsuit_judge]
