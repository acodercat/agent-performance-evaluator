from typing import List, Dict, Any, Union, Tuple, Set 
def sentiment_analysis(text:str, language:str) -> str:
	"""
	sentiment_analysis : Perform sentiment analysis on a given piece of text.    
	Parameters:
	text (str): The text on which to perform sentiment analysis.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	language (str): The language in which the text is written.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [text,language,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def psych_research_get_preference(category:str, option_one:str, option_two:str, demographic:str='all') -> str:
	"""
	psych_research_get_preference : Gathers research data on public preference between two options, based on societal category.    
	Parameters:
	category (str): The societal category the preference data is about. E.g. reading, transportation, food
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	option_one (str): The first option people could prefer.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	option_two (str): The second option people could prefer.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	demographic (str): Specific demographic of society to narrow down the research.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [category,option_one,option_two,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def grocery_store_find_best(my_location:str, products:List[str], rating:float=None) -> str:
	"""
	grocery_store_find_best : Find the closest high-rated grocery stores based on certain product availability.    
	Parameters:
	my_location (str): The current location of the user.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	rating (float): The minimum required store rating. Default is 0.0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	products (List[str]): Required products in a list.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [my_location,products,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def train_random_forest_classifier(dataset:str, max_depth:int, n_estimators:int) -> str:
	"""
	train_random_forest_classifier : Train a Random Forest classifier with the specified parameters.    
	Parameters:
	dataset (str): The dataset to train the classifier on.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	max_depth (int): The maximum depth of the trees in the forest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	n_estimators (int): The number of trees in the forest.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [dataset,max_depth,n_estimators,]

	"""
	return 'Success'

tools = [sentiment_analysis, psych_research_get_preference, grocery_store_find_best, train_random_forest_classifier]
