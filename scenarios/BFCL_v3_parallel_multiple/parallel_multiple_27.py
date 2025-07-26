from typing import List, Dict, Any, Union, Tuple, Set 
def bank_account_transfer(from_account:str, to_account:str, amount:float) -> str:
	"""
	bank_account_transfer : Transfer a given amount from one account to another.    
	Parameters:
	from_account (str): The account to transfer from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	to_account (str): The account to transfer to.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (float): The amount to be transferred.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [from_account,to_account,amount,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def bank_account_calculate_interest(principal:float, rate:float, time:int) -> str:
	"""
	bank_account_calculate_interest : Calculate the amount of interest accrued over a given time period.    
	Parameters:
	principal (float): The initial amount of money.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rate (float): The annual interest rate as a decimal.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The number of years the money is invested for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principal,rate,time,]

	"""
	return 'Success'

tools = [bank_account_transfer, bank_account_calculate_interest]
