import time
import server_state
import server_config


def determine_server_start_time():
	server_state.server_start_time = time.time()


def get_server_start_time():
	return time.asctime(time.localtime(server_state.server_start_time))


def server_shutdown_delay_as_minutes():
	return server_config.server_shutdown_delay_minutes


def server_shutdown_delay_as_seconds():
	return server_config.server_shutdown_delay_minutes*60


def get_current_time():
	return time.asctime(time.localtime(time.time()))