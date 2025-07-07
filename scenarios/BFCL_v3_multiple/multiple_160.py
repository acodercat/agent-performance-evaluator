def get_zodiac_compatibility(sign1, sign2, scale=None):
	"""
	Retrieve the compatibility score between two Zodiac signs.    
	Parameters:
	sign1: The first Zodiac sign.
	sign2: The second Zodiac sign.
	scale: The scale on which compatibility should be shown. Default is 'percentage'.

	"""
	pass

def local_nursery_find(location, plant_types):
	"""
	Locate local nurseries based on location and plant types availability.    
	Parameters:
	location: The city or locality where the nursery needs to be located.
	plant_types: Type of plants the nursery should provide.

	"""
	pass

def get_sculpture_info(artist_name, detail=None):
	"""
	Retrieves the most recent artwork by a specified artist with its detailed description.    
	Parameters:
	artist_name: The name of the artist.
	detail: If True, it provides detailed description of the sculpture. Defaults to False.

	"""
	pass

def monarch_getMonarchOfYear(location, year, fullName='false'):
	"""
	Retrieve the monarch of a specific location during a specified year.    
	Parameters:
	location: The location (e.g., country) whose monarch needs to be found.
	year: The year to search the monarch.
	fullName: If true, returns the full name and title of the monarch.

	"""
	pass

tools = [get_zodiac_compatibility, local_nursery_find, get_sculpture_info, monarch_getMonarchOfYear]
