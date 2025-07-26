from typing import List, Dict, Any, Union, Tuple, Set 
def bank_get_transaction_history(account:str, days:int) -> str:
	"""
	bank_get_transaction_history : Retrieve transaction history for a specific bank account over a specified time frame.    
	Parameters:
	account (str): The account number for which transaction history is required.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	days (int): Number of past days for which to retrieve the transaction history.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [account,days,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def bank_calculate_balance(account:str, transactions:List[Dict[str, Union[float, str]]]=[], starting_balance:float=None) -> str:
	"""
	bank_calculate_balance : Calculate the balance of a specified bank account based on the transactions.    
	Parameters:
	account (str): The account number for which balance is to be calculated.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	transactions (List[Dict[str, Union[float, str]]]): Transaction array Default is empty array.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	starting_balance (float): The starting balance of the account, if known. Default 0.0
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [account,]

	"""
	return 'Success'

tools = [bank_get_transaction_history, bank_calculate_balance]
