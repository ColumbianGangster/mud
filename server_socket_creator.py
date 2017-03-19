#!/usr/bin/python3           # This is server.py file
import socket
import server_config                                         
import server_client_handler
import server_state

# This module creates a server socket. It does not know anything about the configuration.
# If the configuration tells it to reuse a socket address, it will.
# See server_config.py for configuration.

def create_server_socket():
	try:
	    serversocket = socket.socket(server_config.address_family, server_config.socket_type)
	    print ("Socket successfully created")
	    if server_config.reuse_socket_address:
	    	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    if server_config.server_socket_blocking is False:
	    	serversocket.setblocking(False)
	    if server_config.server_socket_timeout_seconds is not None:
	    	serversocket.settimeout(server_config.server_socket_timeout_seconds)
	except socket.error as err:
	    print ("socket creation failed with error %s" %(err))

	# bind to the port
	serversocket.bind((server_config.host, server_config.port))                                  

	# queue up to x requests, where x is the request_queue_size
	serversocket.listen(server_config.request_queue_size)

	print("Server is online on port {}".format(server_config.port))
	server_state.connected = True
	return serversocket