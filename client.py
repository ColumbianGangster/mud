#!/usr/bin/python3           # This is client.py file

import socket
import server_config 
# create a socket object
s = socket.socket(server_config.address_family, server_config.socket_type) 
                          
# connection to hostname on the port.
s.connect((server_config.host, server_config.port))                               
                                  
# Receive no more than 1024 bytes
msg = s.recv(server_config.receive_size)
s.close()
print (msg.decode(server_config.decode_format))
