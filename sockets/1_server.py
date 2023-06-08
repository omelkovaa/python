import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаем IP-адрес сервера и порт для подключения
server_ip = '127.0.0.1'
server_port = 12345

# Подключаемся к серверу
client_socket.connect((server_ip, server_port))
print("Подключение к серверу установлено.")

# Принимаем и отправляем сообщения до получения слова "Пока"
while True:
    # Отправляем сообщение серверу
    message_to_send = input("Введите сообщение для отправки серверу: ")
    client_socket.send(message_to_send.encode())

    # Если отправлено слово "Пока", завершаем связь
    if message_to_send == "Пока":
        break

    # Принимаем сообщение от сервера
    received_message = client_socket.recv(1024).decode()
    print("Получено сообщение от сервера:", received_message)

# Закрываем соединение
client_socket.close()