import socket
import time

ip = 'localhost'
port = 9000
addr = (ip, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

def menu():
    print('1 - Enviar mensagem')
    print('2 - Escutar mensagem')
    print('3 - Enviar mensagem e escutar resposta')
    print('0 - Sair')
    return input('Escolha uma opcao: ')

def enviar_mensagem():
    msg = input('Digite a mensagem: ')
    print('Clientes conectados: 1, 2, 3')
    id_cliente = input('Digite o id do cliente que vai receber: ')
    # Formata mensagem como 'id:mensagem'
    msg = f"{id_cliente}:{msg}"
    client_socket.send(msg.encode()) 

def escutar_mensagem():
    mensagem = client_socket.recv(1024).decode()
    print(f'Mensagem recebida: {mensagem}')

def enviar_e_escutar():
    enviar_mensagem()
    escutar_mensagem() 

while True:
    opcao = menu()
    if opcao == '1':
        enviar_mensagem()
    elif opcao == '2':
        escutar_mensagem()
    elif opcao == '3':
        enviar_e_escutar()
    elif opcao == '0':
        break
    else:
        print('Opcao invalida')

client_socket.close()
