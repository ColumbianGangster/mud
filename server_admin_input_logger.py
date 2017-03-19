import os
import filereading_config
import filepaths

cwd = os.getcwd()

def log(server_admin_input):
	with open(cwd+filepaths.server_admin_command_log_path,filereading_config.append) as server_admin_command_log_file:
		server_admin_command_log_file.write(server_admin_input)