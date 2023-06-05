import socket

# Criação do socket do cliente publisher
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))  # Defina o endereço IP e a porta do servidor

topic = 'noticias'  # Defina o tópico desejado
message = 'publish:' + topic + ':Nova notícia publicada'  # Formato da mensagem: 'publish:topic:mensagem'

# Envia a mensagem para o servidor
client_socket.send(message.encode())
print('Mensagem publicada com sucesso')

# Fecha a conexão com o servidor
client_socket.close()