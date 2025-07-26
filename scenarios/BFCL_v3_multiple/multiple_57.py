from typing import List, Dict, Any, Union, Tuple, Set 
def financial_compound_interest(principle:int, rate:float, time:int, n:int) -> str:
	"""
	financial_compound_interest : Calculates compound interest.    
	Parameters:
	principle (int): The initial amount of money that is being compounded.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rate (float): The annual interest rate, as a decimal. E.g., an annual interest rate of 5% would be represented as 0.05.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The amount of time, in years, that the money is to be compounded for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	n (int): The number of times interest applied per time period.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle,rate,time,n,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def financial_simple_interest(principle:float, rate:float, time:int) -> str:
	"""
	financial_simple_interest : Calculates simple interest.    
	Parameters:
	principle (float): The initial amount of money that interest is being calculated for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rate (float): The annual interest rate, as a decimal. E.g., an annual interest rate of 5% would be represented as 0.05.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	time (int): The amount of time, in years, that the money is to be compounded for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [principle,rate,time,]

	"""
	return 'Success'

tools = [financial_compound_interest, financial_simple_interest]
