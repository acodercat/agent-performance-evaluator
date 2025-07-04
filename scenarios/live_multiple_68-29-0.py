def get_current_weather(location, unit='fahrenheit'):
	"""
	Retrieves the current weather conditions for a specified location.    
	Parameters:
	location: The city and state of the requested weather data, in the format of 'City, State', such as 'San Francisco, CA' or 'New York, NY'.
	unit: The unit of measurement for temperature values.

	"""
	pass

def add_postgres_server(nickname, host, port, database, username, password):
	"""
	Add or create a new Postgres server configuration with the specified parameters.    
	Parameters:
	nickname: A unique identifier for the server configuration.
	host: The hostname or IP address of the Postgres server.
	port: The port number on which the Postgres server is listening.
	database: The name of the default database to connect to.
	username: The username for authentication with the Postgres server.
	password: The password for authentication with the Postgres server.

	"""
	pass

tools = [get_current_weather, add_postgres_server]
