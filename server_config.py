import socket

timeout = None
address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM
request_queue_size = 5
server_admin_request_queue_size = 1 # Probably not be needed.
allow_reuse_address = False
port = 9998
# get local machine name
host = socket.gethostname()
decode_format = 'ascii'
receive_size = 1024
reuse_socket_address = True
server_socket_blocking = True # This must be true, for now.
server_socket_timeout_seconds = 5.0 # seconds. If it does not timeout, then it should be None.
server_shutdown_delay_minutes = 2