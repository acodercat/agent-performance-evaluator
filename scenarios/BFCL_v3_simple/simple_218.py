from typing import List, Dict, Any, Union, Tuple, Set 
def patient_get_mri_report(patient_id:str, status:str, mri_type:str=None) -> str:
	"""
	patient_get_mri_report : Fetch the brain MRI report of the patient for a given status.    
	Parameters:
	patient_id (str): The patient identifier.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	mri_type (str): Type of the MRI. Default to be 'brain'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	status (str): Status of the report, could be 'in progress', 'concluded' or 'draft'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [patient_id,status,]

	"""
	return 'Success'

tools = [patient_get_mri_report]
