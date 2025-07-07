def art_auction_fetch_artwork_price(artwork_name, artist, platform='all'):
	"""
	Fetch the price of a specific artwork on the auction platform.    
	Parameters:
	artwork_name: The name of the artwork to be searched.
	artist: The artist's name to ensure the precise artwork is fetched.
	platform: The platform where the artwork's price should be fetched from.

	"""
	pass

def library_search_book(title, author, platform='all'):
	"""
	Search for a specific book in the library.    
	Parameters:
	title: The title of the book to be searched.
	author: The author of the book to ensure the precise book is fetched.
	platform: The library where the book should be fetched from.

	"""
	pass

tools = [art_auction_fetch_artwork_price, library_search_book]
