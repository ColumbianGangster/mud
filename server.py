#!/usr/bin/python3                                        
import server_client_handler
import server_admin_handler
import server_socket_creator
import server_time_handler

def __listen_for_client_connections_on(serversocket):
	server_client_handler.listen_for_client_connections_on(serversocket)


def __listen_for_server_admin_input():
	server_admin_handler.listen_for_server_admin_input()

def __determine_server_start_time():
	server_time_handler.determine_server_start_time()


def main():
	serversocket = server_socket_creator.create_server_socket()
	__listen_for_client_connections_on(serversocket)
	__listen_for_server_admin_input()
	__determine_server_start_time()
	print("Use Control-C to exit; Or use Control-Break")


if __name__ == "__main__":
     main()