from typing import List, Dict, Any, Union, Tuple, Set 
def calc_Compound_Interest(principle_amount:int, duration:int, annual_rate:float, compound_freq:int=1):
	"""
	calc_Compound_Interest : Compute compound interest.    
	Parameters:
	principle_amount (int): The principle amount that is invested.
	duration (int): Duration of time period in years.
	annual_rate (float): Interest rate in percentage.
	compound_freq (int): The number of times that interest is compounded per unit time.

	Required Parameter = [principle_amount,duration,annual_rate,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def future_value(initial_investment:float, interest_rate:float, time:int, num_compoundings:int=1):
	"""
	future_value : Calculates the future value of an investment given an interest rate and time period.    
	Parameters:
	initial_investment (float): The initial investment amount.
	interest_rate (float): The annual interest rate (as a decimal).
	time (int): The number of time periods the money is invested for.
	num_compoundings (int): The number of times that interest is compounded per time period.

	Required Parameter = [initial_investment,interest_rate,time,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def calc_Simple_Interest(principle_amount:float, duration:float, annual_rate:float):
	"""
	calc_Simple_Interest : Compute simple interest.    
	Parameters:
	principle_amount (float): The principle amount that is invested.
	duration (float): Duration of time period in years.
	annual_rate (float): Interest rate in percentage.

	Required Parameter = [principle_amount,duration,annual_rate,]

	"""
	pass

tools = [calc_Compound_Interest, future_value, calc_Simple_Interest]
