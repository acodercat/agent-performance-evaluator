def releases_api_ReleasesApi_delete_release(releaseId):
	"""
	Deletes a specific release identified by a unique release ID.    
	Parameters:
	releaseId: The unique identifier of the release to be deleted. This is typically a UUID.

	"""
	pass

def releases_api_ReleasesApi_post_release(version, description, is_prerelease=False, release_date='null', release_time='null'):
	"""
	Create a new release in the system, assigning it an unique identifier and storing release metadata.    
	Parameters:
	version: The version number of the release following semantic versioning.
	description: A detailed description of the release contents and changes made.
	is_prerelease: Indicates whether the release is a pre-release version.
	release_date: The date of the release in the format 'YYYY-MM-DD'. If not provided, defaults to the current date.
	release_time: The time of the release in the format 'HH:MM:SS'. If not provided, defaults to the current time.

	"""
	pass

def releases_api_ReleasesApi_put_release(releaseId, releaseName='Unnamed Release', releaseDate=None, isMajorRelease=False):
	"""
	Updates the details of an existing release using the specified release ID.    
	Parameters:
	releaseId: The unique identifier of the release to be updated.
	releaseName: The new name for the release.
	releaseDate: The release date in the format 'YYYY-MM-DD'.
	isMajorRelease: Indicates whether this is a major release.

	"""
	pass

tools = [releases_api_ReleasesApi_delete_release, releases_api_ReleasesApi_post_release, releases_api_ReleasesApi_put_release]
