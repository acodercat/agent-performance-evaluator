def library_search_books(location, genre, title=None):
	"""
	Search for a book in a given library with optional parameters    
	Parameters:
	location: Name or city of library
	genre: Genre of the book
	title: Title of the book. Default ''

	"""
	pass

def google_books_search(genre, title=None):
	"""
	Search for a book in the Google Books library with optional parameters    
	Parameters:
	genre: Genre of the book
	title: Title of the book. Default ''

	"""
	pass

def openlibrary_books_search(genre, title=None):
	"""
	Search for a book in the Open Library with optional parameters    
	Parameters:
	genre: Genre of the book
	title: Title of the book. Default ''

	"""
	pass

tools = [library_search_books, google_books_search, openlibrary_books_search]
