from typing import List, Dict, Any, Union, Tuple, Set 
def database_modify_columns(db_name:str, table:str, operation:str, columns:List[str]) -> str:
	"""
	database_modify_columns : This function allows deletion or addition of columns in a database    
	Parameters:
	db_name (str): The name of the database to modify.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	table (str): The name of the table to modify.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	operation (str): The operation to carry out on the table. Can be 'delete' or 'add'.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	columns (List[str]): List of the columns to add or delete from the table.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [db_name,table,operation,columns,]

	"""
	return 'Success'

from typing import List, Dict, Any, Union, Tuple, Set 
def database_create_backup(db_name:str, backup_location:str, timestamp:bool='False') -> str:
	"""
	database_create_backup : This function creates a backup of the database before modification    
	Parameters:
	db_name (str): The name of the database to create a backup of.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	backup_location (str): The file path where the backup should be stored.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.
	timestamp (bool): Option to append a timestamp to the backup file name.
If you got 'Success' as the return value, it means the function calling is success, you dont need to modify to get the return.

	Required Parameter = [db_name,backup_location,]

	"""
	return 'Success'

tools = [database_modify_columns, database_create_backup]
