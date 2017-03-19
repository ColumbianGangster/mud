import threading
import fileinput
from server_admin_input_parser import parse
from server_admin_input_logger import log
from server_admin_controller import invoke_command_on

class ServerAdminThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		# Listens to a specific client, and sends data as appropriate
	def __listen_for_input(self):
		while True:
			local_data_received = input("> ")
			log(local_data_received)
			parsed_local_data_received = parse(local_data_received)
			invoke_command_on(parsed_local_data_received)

	def run(self):
		print ("Starting " + self.name)
		self.__listen_for_input()
		print ("Exiting " + self.name)


def listen_for_server_admin_input():
	thread = ServerAdminThread("Thread-Server Admin")
	thread.start()