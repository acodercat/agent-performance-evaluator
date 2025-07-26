from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_bmi(weight:int, height:int, system:str=None) -> str:
	"""
	calculate_bmi : Calculate the Body Mass Index (BMI) for a person based on their weight and height.    
	Parameters:
	weight (int): The weight of the person in kilograms.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	height (int): The height of the person in centimeters.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	system (str): The system of units to be used, 'metric' or 'imperial'. Default is 'metric'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [weight,height,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def hotel_booking(hotel_name:str, location:str, start_date:str, end_date:str, rooms:int=1) -> str:
	"""
	hotel_booking : Books a hotel room for a specific date range.    
	Parameters:
	hotel_name (str): The name of the hotel.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	location (str): The city and state, e.g. New York, NY.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	start_date (str): The start date of the reservation. Use format 'YYYY-MM-DD'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	end_date (str): The end date of the reservation. Use format 'YYYY-MM-DD'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rooms (int): The number of rooms to reserve.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [hotel_name,location,start_date,end_date,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def sentiment_analysis(text:str, language:str) -> str:
	"""
	sentiment_analysis : Perform sentiment analysis on a given piece of text.    
	Parameters:
	text (str): The text on which to perform sentiment analysis.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	language (str): The language in which the text is written.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [text,language,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def get_time_difference(place1:str, place2:str) -> str:
	"""
	get_time_difference : Get the time difference between two places.    
	Parameters:
	place1 (str): The first place for time difference.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	place2 (str): The second place for time difference.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [place1,place2,]

	"""
	return 'Success'

tools = [calculate_bmi, hotel_booking, sentiment_analysis, get_time_difference]
