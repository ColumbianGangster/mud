import server_time_handler

# Converts the unix time to asc time
def time():
	print("Server start time: {}".format(server_time_handler.get_server_start_time()))