def delete_apdex_configuration(id):
	"""
	Deletes the Apdex (Application Performance Index) configuration by its unique identifier.    
	Parameters:
	id: The unique identifier of the Apdex configuration to be deleted.

	"""
	pass

def apdex_settings_api_ApdexSettingsApi_create_apdex_configuration(name, thresholds, include_samples=False):
	"""
	Creates a new Apdex (Application Performance Index) configuration for monitoring and assessing the performance of applications.    
	Parameters:
	name: The name of the new Apdex configuration.
	thresholds: Threshold values for categorizing the response times of applications.
	include_samples: Flag to include performance samples in the Apdex calculation.

	"""
	pass

def get_all_apdex_configurations(application_id, include_defaults=True):
	"""
	Retrieve a list of all Apdex score configurations from the system, providing an overview of application performance thresholds.    
	Parameters:
	application_id: Unique identifier of the application for which Apdex configurations are requested.
	include_defaults: Flag to include default Apdex configurations in the response.

	"""
	pass

tools = [delete_apdex_configuration, apdex_settings_api_ApdexSettingsApi_create_apdex_configuration, get_all_apdex_configurations]
