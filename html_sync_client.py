import socket, sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
string = sys.argv[2]
server_ip = sys.argv[1]
while True:
	try:
		client_socket.connect((server_ip, 50001))		
		client_socket.send(string)
		client_socket.close()
		sys.exit()
	except:
		raise	