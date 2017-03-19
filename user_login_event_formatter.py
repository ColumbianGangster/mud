from server_time_handler import get_current_time
from filereading_config import newline


def format(clientsocket,addr):
	return "User connected to server at {} with ip address {} and port {} {}".format(get_current_time, clientsocket, addr, newline)