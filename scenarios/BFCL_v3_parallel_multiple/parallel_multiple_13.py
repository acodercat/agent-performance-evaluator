def temperature_converter_convert(temperature, from_unit, to_unit, round_to=None):
	"""
	Convert a temperature from one unit to another.    
	Parameters:
	temperature: The temperature to convert.
	from_unit: The unit to convert from.
	to_unit: The unit to convert to.
	round_to: The number of decimal places to round the result to. Defaults to 2.

	"""
	pass

def energy_calculator_calculate(substance, mass, initial_temperature, final_temperature, unit=None):
	"""
	Calculate the energy needed to heat a substance from an initial to a final temperature.    
	Parameters:
	substance: The substance to be heated.
	mass: The mass of the substance in grams.
	initial_temperature: The initial temperature of the substance in degrees Celsius.
	final_temperature: The final temperature of the substance in degrees Celsius.
	unit: The unit to report the energy in. Options are 'joules' and 'calories'. Defaults to 'joules'.

	"""
	pass

tools = [temperature_converter_convert, energy_calculator_calculate]
