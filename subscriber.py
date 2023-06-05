import socket

# Criação do socket do cliente subscriber
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))  # Defina o endereço IP e a porta do servidor

topic = 'noticias'  # Defina o tópico desejado
message = 'subscribe:' + topic  # Formato da mensagem: 'subscribe:topic'

# Envia a mensagem para o servidor
client_socket.send(message.encode())

# Recebe a última mensagem do servidor
last_message = client_socket.recv(1024).decode()
if last_message == 'Tópico não encontrado':
    print(f'Tópico {topic} não encontrado')
else:
    print(f'Última mensagem do tópico {topic}: {last_message}')

# Fecha a conexão com o servidor
client_socket.close()