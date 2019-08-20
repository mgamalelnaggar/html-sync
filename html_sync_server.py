import socket, os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 50001))
server_socket.listen(5)

while True:
	try:
		connection,address = server_socket.accept()
		buffer = connection.recv(1024)
		if buffer>0:
			# donot print if running the script in the background (pythonw)
			#print buffer
			
			
			# C:\Program Files (x86)\Google\Chrome\Application\
			# Add the above path in the environment variable to overcome the path with spaces issues
			os.system("Chrome.exe " + str(buffer))
			connection.close()
	except:
		raise
