from typing import List, Dict, Any, Union, Tuple, Set 
def google_books_search(genre:str, title:str=None):
	"""
	google_books_search : Search for a book in the Google Books library with optional parameters    
	Parameters:
	genre (str): Genre of the book
	title (str): Title of the book. Default is not use it if not specified.

	Required Parameter = [genre,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def library_search_books(location:str, genre:str, title:str=None):
	"""
	library_search_books : Search for a book in a given library with optional parameters    
	Parameters:
	location (str): Name or city of library
	genre (str): Genre of the book
	title (str): Title of the book. Default is not use it if not specified.

	Required Parameter = [location,genre,]

	"""
	pass

from typing import List, Dict, Any, Union, Tuple, Set 
def openlibrary_books_search(genre:str, title:str=None):
	"""
	openlibrary_books_search : Search for a book in the Open Library with optional parameters    
	Parameters:
	genre (str): Genre of the book
	title (str): Title of the book. Default is not use it if not specified.

	Required Parameter = [genre,]

	"""
	pass

tools = [google_books_search, library_search_books, openlibrary_books_search]
