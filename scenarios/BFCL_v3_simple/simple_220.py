from typing import List, Dict, Any, Union, Tuple, Set 
def calculate_neuronal_activity(input_synaptic_rate:int, decay_rate:float, weight:float=None) -> str:
	"""
	calculate_neuronal_activity : Calculate the neuronal activity (rate of firing) based on a given input synaptic rate, weight of inputs, and decay rate. Higher input or weight increases firing rate and higher decay rate decreases it.    
	Parameters:
	input_synaptic_rate (int): The synaptic input rate, usually represented as number of inputs per second.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	weight (float): The weight of the input, denoting its influence on the neuron's state. Default is 1.0.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	decay_rate (float): The rate at which the neuron's potential decays in the absence of inputs.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [input_synaptic_rate,decay_rate,]

	"""
	return 'Success'

tools = [calculate_neuronal_activity]
