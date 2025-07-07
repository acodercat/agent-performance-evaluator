def publication_year_find(author, work_title, location=None):
	"""
	Fetches the year a particular scientific work was published.    
	Parameters:
	author: Name of the author of the work.
	work_title: Title of the scientific work.
	location: Place of the publication, if known. Default is 'global'.

	"""
	pass

def portfolio_future_value(stock, invested_amount, expected_annual_return, years):
	"""
	Calculate the future value of an investment in a specific stock based on the invested amount, expected annual return and number of years.    
	Parameters:
	stock: The ticker symbol of the stock.
	invested_amount: The invested amount in USD.
	expected_annual_return: The expected annual return on investment as a decimal. E.g. 5% = 0.05
	years: The number of years for which the investment is made.

	"""
	pass

def religious_history_get_papal_biography(papal_name, include_contributions):
	"""
	Retrieve the biography and main religious and historical contributions of a Pope based on his papal name.    
	Parameters:
	papal_name: The papal name of the Pope.
	include_contributions: Include main contributions of the Pope in the response if true.

	"""
	pass

def board_game_info(game_name, info_required):
	"""
	Get the information about a board game from a database.     
	Parameters:
	game_name: Name of the board game.
	info_required: Array of information requested for the game.

	"""
	pass

tools = [publication_year_find, portfolio_future_value, religious_history_get_papal_biography, board_game_info]
