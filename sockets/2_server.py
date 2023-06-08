import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаем IP-адрес сервера и порт для прослушивания
server_ip = '127.0.0.1'
server_port = 12347

# Привязываем сокет к заданному IP-адресу и порту
server_socket.bind((server_ip, server_port))

# Ожидаем подключение клиента
server_socket.listen(1)
print("Ожидание подключения клиента...")

# Принимаем подключение клиента
client_socket, client_address = server_socket.accept()
print("Подключение установлено:", client_address)

# Принимаем название файла от клиента
file_name = client_socket.recv(1024).decode()
print("Получено название файла от клиента:", file_name)

# Открываем файл и читаем его содержимое
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print("Файл не найден")

# Подсчитываем количество слов
word_count = len(content.split())

# Отправляем количество слов клиенту
client_socket.send(str(word_count).encode())

# Закрываем соединение
client_socket.close()
server_socket.close()