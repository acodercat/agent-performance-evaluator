from typing import List, Dict, Any, Union, Tuple, Set 
def update_user_info(user_id:int, update_info:Dict[str, str], database:str='CustomerInfo') -> str:
	"""
	update_user_info : Update user information in the database.    
	Parameters:
	user_id (int): The user ID of the customer.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	update_info (Dict[str, str]): The new information to update.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	database (str): The database where the user's information is stored.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [user_id,update_info,]

	"""
	return 'Success'

tools = [update_user_info]
