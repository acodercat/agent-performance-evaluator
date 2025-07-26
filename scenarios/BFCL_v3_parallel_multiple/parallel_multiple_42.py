from typing import List, Dict, Any, Union, Tuple, Set 
def book_find(library:str, author:str, genre:str='Sci-Fi', year:int=2000) -> str:
	"""
	book_find : Find a book in a library based on specific criteria like author, genre or publication year.    
	Parameters:
	library (str): The name of the library.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	author (str): Author of the book.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	genre (str): Genre of the book.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	year (int): Year of publication.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [library,author,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def historical_landmark_find(location:str, era:str='Renaissance') -> str:
	"""
	historical_landmark_find : Find historical landmarks based on specific criteria like location or era.    
	Parameters:
	location (str): Location of the landmark.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	era (str): Era of the landmark. E.g. Middle Ages, Renaissance
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [location,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def artwork_find(museum:str, type:str, material:str='', artist:str='') -> str:
	"""
	artwork_find : Locate artwork in museums based on specific criteria like type of material, artist, or era.    
	Parameters:
	museum (str): The name of the museum, e.g. Modern Arts Museum, New York
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	type (str): Type of the artwork. E.g. Painting, Sculpture
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	material (str): Material of the artwork if it's a sculpture. E.g. Bronze, Marble
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	artist (str): Name of the artist.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [museum,type,]

	"""
	return 'Success'

tools = [book_find, historical_landmark_find, artwork_find]
