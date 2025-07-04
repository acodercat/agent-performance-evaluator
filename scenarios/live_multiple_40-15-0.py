def run_microwave(power_level, duration=60, mode='microwave'):
	"""
	Activates the microwave to run at a specified power level.    
	Parameters:
	power_level: The power level at which the microwave should operate.
	duration: The cooking time in seconds.
	mode: The cooking mode such as 'defrost', 'grill', 'convection', or 'microwave'.

	"""
	pass

def oven_preheat(duration, temperature):
	"""
	Preheat the oven for a specified duration at a given temperature.    
	Parameters:
	duration: The duration in minutes to preheat the oven.
	temperature: The temperature in degrees Fahrenheit to preheat the oven.

	"""
	pass

tools = [run_microwave, oven_preheat]
