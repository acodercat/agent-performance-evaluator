from typing import List, Dict, Any, Union, Tuple, Set 
def calc_Simple_Interest(principle_amount:float, duration:float, annual_rate:float) -> str:
	"""
	calc_Simple_Interest : Compute simple interest.    
	Parameters:
	principle_amount (float): The principle amount that is invested.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (float): Duration of time period in years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	annual_rate (float): Interest rate in percentage.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle_amount,duration,annual_rate,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def future_value(initial_investment:float, interest_rate:float, time:int, num_compoundings:int=1) -> str:
	"""
	future_value : Calculates the future value of an investment given an interest rate and time period.    
	Parameters:
	initial_investment (float): The initial investment amount.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	interest_rate (float): The annual interest rate (as a decimal).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The number of time periods the money is invested for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	num_compoundings (int): The number of times that interest is compounded per time period.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [initial_investment,interest_rate,time,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calc_Compound_Interest(principle_amount:float, duration:float, annual_rate:float, compound_freq:int=1) -> str:
	"""
	calc_Compound_Interest : Compute compound interest.    
	Parameters:
	principle_amount (float): The principle amount that is invested.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	duration (float): Duration of time period in years.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	annual_rate (float): Interest rate in percentage.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	compound_freq (int): The number of times that interest is compounded per unit time.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle_amount,duration,annual_rate,]

	"""
	return 'Success'

tools = [calc_Simple_Interest, future_value, calc_Compound_Interest]
