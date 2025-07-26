from typing import List, Dict, Any, Union, Tuple, Set 
def fMRI_analyze(data_source:str, sequence_type:str, smooth:int, voxel_size:int=3) -> str:
	"""
	fMRI_analyze : This function takes in fMRI data to output analyzed data.    
	Parameters:
	data_source (str): The path where the data is stored.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	sequence_type (str): Type of fMRI sequence
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	smooth (int): Spatial smoothing FWHM. In mm.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	voxel_size (int): Size of isotropic voxels in mm.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [data_source,sequence_type,smooth,]

	"""
	return 'Success'

tools = [fMRI_analyze]
