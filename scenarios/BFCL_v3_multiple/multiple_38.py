def library_reserve_book(book_id, branch_id, return_date=None):
	"""
	Reserves a book in the library if available.    
	Parameters:
	book_id: The id of the book to reserve.
	branch_id: The id of the library branch to reserve from.
	return_date: The date the book is to be returned (optional). Default is ''

	"""
	pass

def library_search_book(book_name, city, availability=None, genre=None):
	"""
	Searches for a book in the library within the specified city.    
	Parameters:
	book_name: The name of the book to search for.
	city: The city to search within.
	availability: If true, search for available copies. If false or omitted, search for any copy regardless of availability. Default is false
	genre: The genre of the book to filter search (optional). Default is ''

	"""
	pass

tools = [library_reserve_book, library_search_book]
