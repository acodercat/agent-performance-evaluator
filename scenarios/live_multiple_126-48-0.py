def acl_api_AclApi_retrieve_projects(uuid, excludeInactive=False, onlyRoot=False):
	"""
	Retrieve a list of projects assigned to the specified team, with options to exclude inactive projects and/or omit child projects.    
	Parameters:
	uuid: The unique identifier of the team for which projects are being retrieved.
	excludeInactive: If set to true, inactive projects will not be included in the response.
	onlyRoot: If set to true, only root projects will be returned, excluding their child projects.

	"""
	pass

def analysis_api_AnalysisApi_retrieve_analysis(project, component, vulnerability):
	"""
	Retrieves the detailed analysis trail for a given project, component, and vulnerability.    
	Parameters:
	project: The unique identifier (UUID) of the project for which the analysis trail is retrieved.
	component: The unique identifier (UUID) of the component associated with the project.
	vulnerability: The unique identifier (UUID) of the vulnerability within the component.

	"""
	pass

tools = [acl_api_AclApi_retrieve_projects, analysis_api_AnalysisApi_retrieve_analysis]
