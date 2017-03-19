#!/usr/bin/python3 

from server_config import request_queue_size
from server_config import server_admin_request_queue_size
from landing import get_landing_string
import threading
import server_client_handler_threaded_strategy

# Documentation:
# http://chriskiehl.com/article/parallelism-in-one-line/
# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

# This module determines which threaded strategy to use.

def __threaded_approach(serversocket):
	server_client_handler_threaded_strategy.run(serversocket)

def __unthreaded_simple_approach(serversocket):
	# establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    # msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(get_landing_string().encode('ascii'))
    clientsocket.close()


# This method abstracts away how the client is handled. 
# Users of this module do not know how the multi threading is handled, if at all.
def listen_for_client_connections_on(serversocket):
	__threaded_approach(serversocket)