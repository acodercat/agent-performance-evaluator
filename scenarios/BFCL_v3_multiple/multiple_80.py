def music_shop_find_nearby(location, services=None, instruments=None):
	"""
	Locate nearby music shops based on specific criteria like instrument lessons availability.    
	Parameters:
	location: The city and state, e.g. Nashville, TN
	services: Types of instrument lessons offered in the shop. Default empty array
	instruments: Types of instruments sold in the shop. Default empty array

	"""
	pass

def gym_find_nearby(location, classes=None, equipment=None):
	"""
	Locate nearby gyms based on specific criteria like types of fitness classes availability.    
	Parameters:
	location: The city and state, e.g. Nashville, TN
	classes: Types of fitness classes offered in the gym. Default empty array
	equipment: Types of gym equipment available. Default empty array

	"""
	pass

tools = [music_shop_find_nearby, gym_find_nearby]
