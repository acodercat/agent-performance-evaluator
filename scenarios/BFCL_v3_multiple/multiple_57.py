from typing import List, Dict, Any, Union, Tuple 
def financial_compound_interest(principle:int, rate:float, time:int, n:int):
	"""
	financial_compound_interest : Calculates compound interest.    
	Parameters:
	principle (int): The initial amount of money that is being compounded.
	rate (float): The annual interest rate, as a decimal. E.g., an annual interest rate of 5% would be represented as 0.05.
	time (int): The amount of time, in years, that the money is to be compounded for.
	n (int): The number of times interest applied per time period.

	Required Parameter = [principle,rate,time,n,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple 
def financial_simple_interest(principle:float, rate:float, time:int):
	"""
	financial_simple_interest : Calculates simple interest.    
	Parameters:
	principle (float): The initial amount of money that interest is being calculated for.
	rate (float): The annual interest rate, as a decimal. E.g., an annual interest rate of 5% would be represented as 0.05.
	time (int): The amount of time, in years, that the money is to be compounded for.

	Required Parameter = [principle,rate,time,]

	"""
	pass

tools = [financial_compound_interest, financial_simple_interest]
