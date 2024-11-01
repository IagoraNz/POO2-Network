import socket

host = 'localhost'
port = 9000
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(3) 

print('Aguardando conexão dos clientes...')

connections = {}

for i in range(1, 4):
    con, client = serv_socket.accept()
    connections[i] = con
    print(f'Cliente {i} conectado')

print('Clientes conectados: 1, 2, 3')

while True:
    for client_id, con in connections.items():
        try:
            data = con.recv(1024)
            if data:
                decoded_data = data.decode()
                print(f'Mensagem recebida de {client_id}: {decoded_data}')

                id_cliente, msg = decoded_data.split(':')
                id_cliente = int(id_cliente)
                
                if msg == 'exit':
                    print(f'Cliente {id_cliente} desconectado')
                    connections[id_cliente].close()
                    del connections[id_cliente]
                    break 
                else:
                    if id_cliente in connections:
                        connections[id_cliente].send(f'{client_id}:{msg}'.encode())
        except ConnectionResetError:
            print(f'Cliente {client_id} desconectado abruptamente')
            con.close()
            del connections[client_id]
            break 

    if not connections:
        print("Todos os clientes se desconectaram.")
        break

serv_socket.close()
