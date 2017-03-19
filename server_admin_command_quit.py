import sys
from server_time_handler import server_shutdown_delay_as_minutes
from server_time_handler import server_shutdown_delay_as_seconds
import time


def quit():
	__broadcast_global_message("Server is shutting down in {}} minutes."
		.format(server_shutdown_delay_as_minutes()))

	__wait(server_shutdown_delay_as_seconds()/2)

	__broadcast_global_message("Server is shutting down in {}} minutes."
		.format(server_shutdown_delay_as_minutes()/2))

	__wait(server_time_handler.server_shutdown_delay_as_seconds()/2)

	__gracefully_disconnect_players()

	__save_world_state()

	server_state.connected = False

	sys.exit(0)


def __save_world_state():
	print("TODO: Save world state needs an implementation")


def __broadcast_global_message(msg):
	print("TODO: Broadcast Global Message needs an implementation")


def __gracefully_disconnect_players():
	print("TODO: Gracefully Disconnect Players needs an implementation")


def __wait(seconds):
	time.sleep(seconds)