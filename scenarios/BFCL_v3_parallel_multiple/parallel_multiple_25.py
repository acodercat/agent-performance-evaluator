from typing import List, Dict, Any, Union, Tuple, Set 
def stock_invest_calculate_investment_cost(company:str, shares:int) -> str:
	"""
	stock_invest_calculate_investment_cost : Calculate the cost of investing in a specific number of shares from a given company.    
	Parameters:
	company (str): The company that you want to invest in.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	shares (int): Number of shares to invest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [company,shares,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def stock_invest_calculate_dividend_payout(shares:int, dividend_per_share:float) -> str:
	"""
	stock_invest_calculate_dividend_payout : Calculate the total dividend payout for a specific number of shares with known dividend per share.    
	Parameters:
	shares (int): Number of shares to calculate dividends.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	dividend_per_share (float): Known dividend per share.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [shares,dividend_per_share,]

	"""
	return 'Success'

tools = [stock_invest_calculate_investment_cost, stock_invest_calculate_dividend_payout]
