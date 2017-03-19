import user_login_event_logger
import user_login_event_formatter
from socket import timeout
import server_state
from specific_client_thread import SpecificClientThread


def listen_for_clients(serversocket):
	# Listen for new clients and create a thread when they connect
	# def __new_client_listener(serversocket):
	print("Listening for new clients and create a thread when they connect...")
	while server_state.connected:
		try:
			clientsocket,addr = serversocket.accept()
			user_login_event_logger.log(user_login_event_formatter.format(clientsocket, addr))
			__listen_to_new_client(clientsocket, addr)
			server_state.number_of_clients_since_server_start = server_state.number_of_clients_since_server_start + 1
		except timeout:
			pass


def __listen_to_new_client(clientsocket, addr):

	thread = SpecificClientThread(
		server_state.number_of_clients_since_server_start, 
		"Thread-"+str(server_state.number_of_clients_since_server_start),
		clientsocket,
		addr)

	thread.start()