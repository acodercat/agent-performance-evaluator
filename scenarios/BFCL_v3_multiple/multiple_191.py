def random_normalvariate(mu, sigma):
	"""
	Generates a random number from a normal distribution given the mean and standard deviation.    
	Parameters:
	mu: Mean of the normal distribution.
	sigma: Standard deviation of the normal distribution.

	"""
	pass

def get_personality_traits(type, traits=None):
	"""
	Retrieve the personality traits for a specific personality type, including their strengths and weaknesses.    
	Parameters:
	type: The personality type.
	traits: List of traits to be retrieved, default is ['strengths', 'weaknesses'].

	"""
	pass

def elephant_population_estimate(current_population, growth_rate, years):
	"""
	Estimate future population of elephants given current population and growth rate.    
	Parameters:
	current_population: The current number of elephants.
	growth_rate: The annual population growth rate of elephants.
	years: The number of years to project the population.

	"""
	pass

def book_hotel(hotel_name, location, room_type, start_date, stay_duration, view='No preference'):
	"""
	Book a room in a specific hotel with particular preferences    
	Parameters:
	hotel_name: The name of the hotel.
	location: The location of the hotel.
	room_type: The type of room preferred.
	start_date: The starting date of the stay in format MM-DD-YYYY.
	stay_duration: The duration of the stay in days.
	view: The preferred view from the room, can be ignored if no preference. If none provided, assumes no preference.

	"""
	pass

tools = [random_normalvariate, get_personality_traits, elephant_population_estimate, book_hotel]
