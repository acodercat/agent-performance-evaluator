from typing import List, Dict, Any, Union, Tuple, Set 
def investment_withdraw(company:str, amount:float) -> str:
	"""
	investment_withdraw : Withdraw a specific amount from a company's stock.    
	Parameters:
	company (str): The company you want to withdraw from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (float): The amount you want to withdraw.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,amount,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def investment_invest(company:str, amount:float) -> str:
	"""
	investment_invest : Invest a specific amount in a company's stock.    
	Parameters:
	company (str): The company you want to invest in.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	amount (float): The amount you want to invest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,amount,]

	"""
	return 'Success'

tools = [investment_withdraw, investment_invest]
