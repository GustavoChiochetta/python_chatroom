import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8888))

done = False

print('Seja bem vindo ao suporte da Almourol!')
name = str(input('Por favor nos diga seu nome: '))
print('Iremos iniciar seu atendimento ', name)
client.send(f"Conectando com o cliente {name}".encode('utf-8'))

while not done:
    client.send(input(f"{name}: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'sair':
        done = True
    else:
        print('Suporte: ', msg)
