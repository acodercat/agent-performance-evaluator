from typing import List, Dict, Any, Union, Tuple, Set 
def send_email(to:str, subject:str, body:str, cc:str=None, bcc:str=None) -> str:
	"""
	send_email : Send an email to the specified email address.    
	Parameters:
	to (str): The email address to send to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	subject (str): The subject of the email.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	body (str): The body content of the email.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	cc (str): The email address to carbon copy. Default is empty if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	bcc (str): The email address to blind carbon copy. Default is empty if not specified.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [to,subject,body,]

	"""
	return 'Success'

tools = [send_email]
