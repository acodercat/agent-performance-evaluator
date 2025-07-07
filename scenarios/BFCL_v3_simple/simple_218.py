def patient_get_mri_report(patient_id, status, mri_type=None):
	"""
	Fetch the brain MRI report of the patient for a given status.    
	Parameters:
	patient_id: The patient identifier.
	mri_type: Type of the MRI. Default to be 'brain'.
	status: Status of the report, could be 'in progress', 'concluded' or 'draft'.

	"""
	pass

tools = [patient_get_mri_report]
