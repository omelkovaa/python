import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаем IP-адрес сервера и порт для прослушивания
server_ip = '127.0.0.1'
server_port = 12345

# Привязываем сокет к заданному IP-адресу и порту
server_socket.bind((server_ip, server_port))

# Ожидаем подключение клиента
server_socket.listen(1)
print("Ожидание подключения клиента...")

# Принимаем подключение клиента
client_socket, client_address = server_socket.accept()
print("Подключение установлено:", client_address)

# Принимаем и отправляем сообщения до получения слова "Пока"
while True:
    # Принимаем сообщение от клиента
    received_message = client_socket.recv(1024).decode()
    print("Получено сообщение от клиента:", received_message)

    # Если получено слово "Пока", завершаем связь
    if received_message == "Пока":
        break

    # Отправляем сообщение клиенту
    message_to_send = input("Введите сообщение для отправки клиенту: ")
    client_socket.send(message_to_send.encode())

# Закрываем соединение
client_socket.close()
server_socket.close()