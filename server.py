import socket

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))  # Defina o endereço IP e a porta desejados
server_socket.listen(5)  # Número máximo de conexões pendentes

topics = {}  # Dicionário para armazenar os tópicos e suas mensagens

print('Servidor iniciado. Aguardando conexões...')

while True:
    # Aceita a conexão do cliente
    client_socket, address = server_socket.accept()
    print(f'Conexão estabelecida com {address[0]}:{address[1]}')

    # Recebe a mensagem do cliente
    message = client_socket.recv(1024).decode()
    message_parts = message.split(':')
    action = message_parts[0].lower()
    topic = message_parts[1].lower()

    if action == 'publish':
        # Armazena a mensagem no tópico correspondente
        if topic in topics:
            topics[topic] = message_parts[2]
        else:
            topics[topic] = ''

        print(f'Mensagem publicada no tópico {topic}')

    elif action == 'subscribe':
        # Verifica se o tópico existe
        if topic in topics:
            # Envia a última mensagem armazenada no tópico para o cliente
            last_message = topics[topic]
            client_socket.send(last_message.encode())
            print(f'Enviada a última mensagem do tópico {topic} para {address[0]}:{address[1]}')
        else:
            # Tópico não existe
            client_socket.send('Tópico não encontrado'.encode())
            print(f'Tópico {topic} não encontrado. Mensagem enviada para {address[0]}:{address[1]}')

    # Fecha a conexão com o cliente
    client_socket.close()