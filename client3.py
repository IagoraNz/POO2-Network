import socket
ip = 'localhost'
port = 9000
addr = ((ip,port)) #define a tupla de endereco
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
client_socket.connect(addr) #realiza a conexao
while(True):
    mensagem = input('Digite uma mensagem para enviar ao servidor: ')
    client_socket.send(mensagem.encode()) #envia mensagem
    print ('Mensagem enviada')
    print(client_socket.recv(1024).decode())

client_socket.close() #fecha a conexao