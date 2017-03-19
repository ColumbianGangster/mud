from landing import get_landing_string
import threading

class SpecificClientThread (threading.Thread):
	def __init__(self, threadID, name, clientsocket, addr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.clientsocket = clientsocket
		self.addr = addr
		# Listens to a specific client, and sends data as appropriate
	def __specific_client_listener(self,clientsocket, addr):
		print("Got a connection from %s" % str(addr))
		clientsocket.send(get_landing_string().encode('ascii'))
		clientsocket.close()
	def run(self):
		print ("Starting " + self.name)
		self.__specific_client_listener(self.clientsocket, self.addr)
		print ("Exiting " + self.name)