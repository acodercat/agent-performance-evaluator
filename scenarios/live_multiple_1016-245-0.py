def create_global_application_alert_config(name, alert_type, threshold, recipients, enabled=True):
	"""
	Create a new global application alert configuration setting for monitoring and notifications.    
	Parameters:
	name: A unique name identifying the alert configuration.
	alert_type: The type of alert to be configured.
	threshold: The value at which the alert should be triggered. Units depend on the alert_type.
	recipients: A list of email addresses to notify when the alert is triggered.
	enabled: Flag indicating whether the alert configuration is enabled or not.

	"""
	pass

def enable_global_application_alert_config(id):
	"""
	Activate the global alert configuration for an application using the specified identifier.    
	Parameters:
	id: The unique identifier of the application alert configuration to be enabled.

	"""
	pass

def create_mobile_app_alert_config(app_id, alert_name, threshold, recipients, severity='low', enabled=True):
	"""
	Creates a configuration for mobile app alerts, specifying the conditions and recipients for notifications.    
	Parameters:
	app_id: The unique identifier of the mobile application.
	alert_name: A descriptive name for the alert.
	threshold: The numerical value at which the alert should be triggered.
	recipients: A list of email addresses that will receive the alert.
	severity: The severity level of the alert.
	enabled: A flag indicating whether the alert configuration is active.

	"""
	pass

tools = [create_global_application_alert_config, enable_global_application_alert_config, create_mobile_app_alert_config]
