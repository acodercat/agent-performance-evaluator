def database_modify_columns(db_name, table, operation, columns):
	"""
	This function allows deletion or addition of columns in a database    
	Parameters:
	db_name: The name of the database to modify.
	table: The name of the table to modify.
	operation: The operation to carry out on the table. Can be 'delete' or 'add'.
	columns: List of the columns to add or delete from the table.

	"""
	pass

def database_create_backup(db_name, backup_location, timestamp='False'):
	"""
	This function creates a backup of the database before modification    
	Parameters:
	db_name: The name of the database to create a backup of.
	backup_location: The file path where the backup should be stored.
	timestamp: Option to append a timestamp to the backup file name.

	"""
	pass

tools = [database_modify_columns, database_create_backup]
