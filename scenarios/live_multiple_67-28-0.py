def get_current_weather(location, unit='fahrenheit'):
	"""
	Fetches the current weather data for a specified location, with an option to select the temperature unit.    
	Parameters:
	location: The location for which to get the weather, in the format of 'City, State', such as 'San Francisco, CA' or 'New York, NY'.
	unit: The temperature unit in which to display the weather data.

	"""
	pass

def add_postgres_server(host, username, password, port=5432, database='postgres'):
	"""
	Adds or creates a new PostgreSQL server configuration to connect to a database instance.    
	Parameters:
	host: The hostname or IP address of the PostgreSQL server.
	port: The port number on which the PostgreSQL server is listening.
	database: The name of the database to connect to.
	username: The username for authenticating with the PostgreSQL server.
	password: The password for authenticating with the PostgreSQL server.

	"""
	pass

tools = [get_current_weather, add_postgres_server]
