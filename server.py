import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()

client, addr = server.accept()

done = False
first = True

while first:
    msg = client.recv(1024).decode('utf-8')
    name = msg.split()[-1]
    if "Conectando com o cliente" in msg:
        print(msg)
        print("Aguardando mensagem...")
        first = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'sair':
        done = True
        client.send("sair".encode('utf-8'))
    else:
        print(f"{name}: ", msg)
        client.send(input('Suporte: ').encode('utf-8'))
