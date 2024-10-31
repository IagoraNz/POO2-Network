import socket

ip = ''
port = 900
addr = ((ip, port))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr)
server_socket.listen(10)
print('listening on', addr)
connection, client_addr = server_socket.accept()
print('connection from', client_addr)
