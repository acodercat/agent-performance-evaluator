def get_sculpture_info(artist_name, detail=None):
	"""
	Retrieves the most recent artwork by a specified artist with its detailed description.    
	Parameters:
	artist_name: The name of the artist.
	detail: If True, it provides detailed description of the sculpture. Defaults to False.

	"""
	pass

def find_exhibition(location, art_form, month=None, user_ratings=None):
	"""
	Locate the most popular exhibitions based on criteria like location, time, art form, and user ratings.    
	Parameters:
	location: The city where the exhibition is held, e.g., New York, NY.
	art_form: The form of art the exhibition is displaying e.g., sculpture.
	month: The month of exhibition. Default value will return upcoming events.
	user_ratings: Select exhibitions with user rating threshold. Default is 'average'.

	"""
	pass

def card_game_probability_calculate(total_cards, desired_cards, cards_drawn=1):
	"""
	Calculate the probability of drawing a certain card or suit from a deck of cards.    
	Parameters:
	total_cards: Total number of cards in the deck.
	desired_cards: Number of cards in the deck that satisfy the conditions.
	cards_drawn: Number of cards drawn from the deck.

	"""
	pass

tools = [get_sculpture_info, find_exhibition, card_game_probability_calculate]
