from typing import List, Dict, Any, Union, Tuple, Set 
def calc_heat_capacity(temp:int, volume:int, gas:str=None) -> str:
	"""
	calc_heat_capacity : Calculate the heat capacity at constant pressure of air using its temperature and volume.    
	Parameters:
	temp (int): The temperature of the gas in Kelvin.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	volume (int): The volume of the gas in m^3.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	gas (str): Type of gas, with air as default.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [temp,volume,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_discounted_cash_flow(coupon_payment:float, period:int, discount_rate:float, face_value:int=None) -> str:
	"""
	calculate_discounted_cash_flow : Calculate the discounted cash flow of a bond for a given annual coupon payment, time frame and discount rate.    
	Parameters:
	coupon_payment (float): The annual coupon payment.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	period (int): The time frame in years for which coupon payment is made.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	discount_rate (float): The discount rate.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	face_value (int): The face value of the bond, default is $1000.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [coupon_payment,period,discount_rate,]

	"""
	return 'Success'

tools = [calc_heat_capacity, calculate_discounted_cash_flow]
