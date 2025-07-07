def video_games_store_currency(platform, region='True'):
	"""
	Fetches the currency used in a specific region in a gaming platform store.    
	Parameters:
	platform: The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
	region: The region e.g. United States, United Kingdom, Japan

	"""
	pass

def video_games_on_sale(game_title, platform, region=None):
	"""
	Checks if a particular game is currently on sale in a specific gaming platform store and in a specific region.    
	Parameters:
	game_title: The title of the video game
	platform: The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
	region: The region e.g. United States, United Kingdom, Japan. Default United States

	"""
	pass

def video_games_store_price(game_title, platform, region=None):
	"""
	Fetches the selling price of a specified game in a particular gaming platform store and in a specific region.    
	Parameters:
	game_title: The title of the video game
	platform: The gaming platform e.g. PlayStation, Xbox, Nintendo Switch
	region: The region e.g. United States, United Kingdom, Japan. Default to United States

	"""
	pass

tools = [video_games_store_currency, video_games_on_sale, video_games_store_price]
