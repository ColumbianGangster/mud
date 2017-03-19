from listen_for_clients_thread import ListenForClientsThread

def run(serversocket):
	thread = ListenForClientsThread("ListenForClientsThread", serversocket)
	thread.start()


	# from multiprocessing.dummy import Pool as ThreadPool
	# start_new_thread(__new_client_listener, ("serversocket", serversocket))

	# # Make the initial pool of workers
	# pool = ThreadPool(request_queue_size + server_admin_request_queue_size)

	# results = pool.map(urllib2.urlopen, urls)
	# #close the pool and wait for the work to finish 
	# pool.close() 
	# pool.join()