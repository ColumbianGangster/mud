import os
import filereading_config
import filepaths

cwd = os.getcwd()

def log(line):
	with open(cwd+filepaths.user_login_event_log_path, filereading_config.append) as f:
		f.write(line)