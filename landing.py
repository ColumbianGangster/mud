import os
import filereading_config
import filepaths


cwd = os.getcwd()
# .read() returns the entire contents of the file as a single string.
# .readline() returns the next line of the file, returning the text up to and including the next newline character
# .readlines()  returns a list of the lines in the file, where each item of the list represents a single line.
def get_landing_string():
	landing_file = open(cwd+filepaths.landing_path,filereading_config.read_only)
	landing_string = landing_file.read()
	landing_file.close()
	return landing_string

