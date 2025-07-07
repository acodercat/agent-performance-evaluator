def dice_roll_probability(desired_sum, sides_per_die, n_rolls=None):
	"""
	Calculate the probability of a specific sum appearing from rolling two dice.    
	Parameters:
	desired_sum: The sum for which to calculate the probability.
	n_rolls: Number of dice to be rolled. Default is 1
	sides_per_die: Number of sides on each die.

	"""
	pass

def flip_coin_probability(desired_outcome, n_flips=None):
	"""
	Calculate the probability of a specific outcome appearing from flipping a coin.    
	Parameters:
	desired_outcome: The outcome for which to calculate the probability.
	n_flips: Number of coins to be flipped. Default 1

	"""
	pass

def shuffle_card_probability(desired_card, n_decks=None):
	"""
	Calculate the probability of a specific card appearing from a shuffled deck.    
	Parameters:
	desired_card: The card for which to calculate the probability.
	n_decks: Number of decks to shuffle. Default 1

	"""
	pass

tools = [dice_roll_probability, flip_coin_probability, shuffle_card_probability]
