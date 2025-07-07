def hotel_booking(location, room_type, duration, start_date, preferences=None):
	"""
	Books a hotel room given the location, room type, stay duration and any additional preferences.    
	Parameters:
	location: The city where you want to book the hotel.
	room_type: Type of the room required. Options: 'single', 'double', 'deluxe', etc.
	duration: The number of nights you want to book the hotel for.
	start_date: The date when your stay begins.
	preferences: Optional preferences of stay at the hotel. Default is all if not specified.

	"""
	pass

def soccer_get_last_match(team_name, include_stats=None):
	"""
	Retrieve the details of the last match played by a specified soccer club.    
	Parameters:
	team_name: The name of the soccer club.
	include_stats: If true, include match statistics like possession, shots on target etc. Default is false.

	"""
	pass

def calculate_BMI(weight_kg, height_m):
	"""
	Calculate the Body Mass Index (BMI) given a person's weight and height.    
	Parameters:
	weight_kg: The weight of the person in kilograms.
	height_m: The height of the person in meters.

	"""
	pass

tools = [hotel_booking, soccer_get_last_match, calculate_BMI]
