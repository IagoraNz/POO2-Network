import socket

host = '192.168.68.164'
port = 9000
addr = (host, port)

# Configuração do servidor
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(2)  # Limite de 2 conexões

print('Aguardando conexão dos clientes...')

# Aceita as duas conexões
con1, cliente1 = serv_socket.accept()
print('Cliente 1 conectado, aguardando Cliente 2...')
con2, cliente2 = serv_socket.accept()
print('Cliente 2 conectado!')

print('Aguardando mensagens...')

# Loop principal para alternar entre as conexões
while True:
    # Recebe a mensagem do Cliente 1 e encaminha para Cliente 2
    try:
        recebe1 = con1.recv(1024)
        if not recebe1:
            print("Cliente 1 desconectou.")
            break  # Encerra o loop se Cliente 1 desconectar
        print('Mensagem recebida de Cliente 1:', recebe1.decode())
        con1.send('Mensagem recebida'.encode())  # Confirma recebimento a Cliente 1
        con2.send(recebe1)  # Repassa a mensagem para Cliente 2
    except ConnectionResetError:
        print("Cliente 1 desconectou.")
        break

    # Recebe a mensagem do Cliente 2 e encaminha para Cliente 1
    try:
        recebe2 = con2.recv(1024)
        if not recebe2:
            print("Cliente 2 desconectou.")
            break  # Encerra o loop se Cliente 2 desconectar
        print('Mensagem recebida de Cliente 2:', recebe2.decode())
        con2.send('Mensagem recebida'.encode())  # Confirma recebimento a Cliente 2
        con1.send(recebe2)  # Repassa a mensagem para Cliente 1
    except ConnectionResetError:
        print("Cliente 2 desconectou.")
        break

# Fecha as conexões
con1.close()
con2.close()
serv_socket.close()
