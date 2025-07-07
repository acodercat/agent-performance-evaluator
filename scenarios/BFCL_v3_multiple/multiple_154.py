def US_president_in_year(year, full_name=True):
	"""
	Retrieve the name of the U.S. president in a given year.    
	Parameters:
	year: The year in question.
	full_name: Option to return full name with middle initial, if applicable.

	"""
	pass

def find_card_in_deck(rank, suit, deck=None):
	"""
	Locate a particular card in a deck based on rank and suit.    
	Parameters:
	rank: Rank of the card (e.g. Ace, Two, King).
	suit: Suit of the card (e.g. Hearts, Spades, Diamonds, Clubs).
	deck: Deck of cards. If not provided, the deck will be a standard 52 card deck by default

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

def update_user_info(user_id, update_info, database='CustomerInfo'):
	"""
	Update user information in the database.    
	Parameters:
	user_id: The user ID of the customer.
	update_info: The new information to update.
	database: The database where the user's information is stored.

	"""
	pass

tools = [US_president_in_year, find_card_in_deck, soccer_get_last_match, update_user_info]
