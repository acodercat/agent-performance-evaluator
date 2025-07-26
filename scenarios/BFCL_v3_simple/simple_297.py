from typing import List, Dict, Any, Union, Tuple, Set 
def music_theory_chordProgression(progression:List[str], returnAllPossibleKeys:bool=None, assumeMajor:bool=None) -> str:
	"""
	music_theory_chordProgression : Identifies a potential key signature for the given chord progression.    
	Parameters:
	progression (List[str]): The chord progression in Roman numerals. Eg: ['I', 'V', 'vi', 'IV'].
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	returnAllPossibleKeys (bool): Flag indicating if the function should return all possible key signatures that fit the chord progression. If false, the function will return the first valid key it finds. Default is false.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	assumeMajor (bool): Assumption if the key signature is Major. If true, the function will assume the key signature to be major and otherwise minor. Default is true.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [progression,]

	"""
	return 'Success'

tools = [music_theory_chordProgression]
