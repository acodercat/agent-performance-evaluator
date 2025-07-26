from typing import List, Dict, Any, Union, Tuple, Set 
def library_search_book(book_name:str, city:str, availability:bool=None, genre:str='') -> str:
	"""
	library_search_book : Searches for a book in the library within the specified city.    
	Parameters:
	book_name (str): The name of the book to search for.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	city (str): The city to search within.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	availability (bool): If true, search for available copies. If false or omitted, search for any copy regardless of availability. Default false
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	genre (str): The genre of the book to filter search (optional).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [book_name,city,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def library_reserve_book(book_id:str, branch_id:str, return_date:str='') -> str:
	"""
	library_reserve_book : Reserves a book in the library if available.    
	Parameters:
	book_id (str): The id of the book to reserve.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	branch_id (str): The id of the library branch to reserve from.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	return_date (str): The date the book is to be returned (optional).
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [book_id,branch_id,]

	"""
	return 'Success'

tools = [library_search_book, library_reserve_book]
