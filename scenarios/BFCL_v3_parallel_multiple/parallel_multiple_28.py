def criminal_record_get_offense_nature(criminal_name, optional_param=None):
	"""
	Get details about the nature of offenses committed by a criminal.    
	Parameters:
	criminal_name: Name of the criminal.
	optional_param: Optionally retrieve additional details, by default this is set to false.

	"""
	pass

def criminal_record_get_status(criminal_name, region):
	"""
	Find the conviction status of a criminal in a specified region.    
	Parameters:
	criminal_name: Name of the criminal.
	region: Region where criminal record is to be searched.

	"""
	pass

tools = [criminal_record_get_offense_nature, criminal_record_get_status]
