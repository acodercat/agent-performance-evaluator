from typing import List, Dict, Any, Union, Tuple 
def fMRI_analyze(data_source:str, sequence_type:str, smooth:int, voxel_size:int=3):
	"""
	fMRI_analyze : This function takes in fMRI data to output analyzed data.    
	Parameters:
	data_source (str): The path where the data is stored.
	sequence_type (str): Type of fMRI sequence
	smooth (int): Spatial smoothing FWHM. In mm.
	voxel_size (int): Size of isotropic voxels in mm.

	Required Parameter = [data_source,sequence_type,smooth,]

	"""
	pass

tools = [fMRI_analyze]
