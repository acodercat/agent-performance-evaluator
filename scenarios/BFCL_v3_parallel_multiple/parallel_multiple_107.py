def google_books_search(genre, title=None):
	"""
	Search for a book in the Google Books library with optional parameters    
	Parameters:
	genre: Genre of the book
	title: Title of the book. Default is not use it if not specified.

	"""
	pass

def library_search_books(location, genre, title=None):
	"""
	Search for a book in a given library with optional parameters    
	Parameters:
	location: Name or city of library
	genre: Genre of the book
	title: Title of the book. Default is not use it if not specified.

	"""
	pass

def openlibrary_books_search(genre, title=None):
	"""
	Search for a book in the Open Library with optional parameters    
	Parameters:
	genre: Genre of the book
	title: Title of the book. Default is not use it if not specified.

	"""
	pass

tools = [google_books_search, library_search_books, openlibrary_books_search]
