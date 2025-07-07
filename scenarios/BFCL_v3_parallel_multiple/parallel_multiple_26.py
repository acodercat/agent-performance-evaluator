def bank_get_transaction_history(account, days):
	"""
	Retrieve transaction history for a specific bank account over a specified time frame.    
	Parameters:
	account: The account number for which transaction history is required.
	days: Number of past days for which to retrieve the transaction history.

	"""
	pass

def bank_calculate_balance(account, transactions=[], starting_balance=None):
	"""
	Calculate the balance of a specified bank account based on the transactions.    
	Parameters:
	account: The account number for which balance is to be calculated.
	transactions: Transaction array Default is empty array.
	starting_balance: The starting balance of the account, if known. Default 0.0

	"""
	pass

tools = [bank_get_transaction_history, bank_calculate_balance]
