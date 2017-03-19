import threading
from server_clients_listener import listen_for_clients


# Listens to a specific client
class ListenForClientsThread(threading.Thread):


	def __init__(self, threadID, serversocket):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.serversocket = serversocket


	def run(self):
		print ("Starting " + self.threadID)
		listen_for_clients(self.serversocket)
		print ("Exiting " + self.threadID)