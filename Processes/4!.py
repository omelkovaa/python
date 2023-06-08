"""
Запустите фоновый процесс который следит за сроком подписки пользователя
(для примера 10 секунд) если время подписки вышло выведите надпись
"Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с
пользователем в игру "угадай число".
"""

# Импортируем необходимые модули
from multiprocessing import Process, Pipe
from time import sleep
from random import randint

# Генерируем случайное число для игры и устанавливаем время подписки
num = randint(1, 10)
time = 3

# Функция, которая запускается в отдельном процессе и отслеживает время подписки
def subscription(time, conn):
    while time != 0:
        sleep(1)
        time -= 1
    print("\nВремя вашей подписки истекло")
    conn.send(True)
    conn.close()
    return

# Функция для игры "угадай число"
def game(num, conn):
    count = 1
    while True:
        # Проверяем, не закончилась ли подписка
        if conn.poll():
            conn.close()
            return
        inp = int(input("Введите число: "))
        if inp == num:
            print(f"Вы угадали число с {count} попытки")
            sleep(0.5)
            # Генерируем новое число для продолжения игры
            num2 = randint(1, 10)
            return game(num2, conn)
        else:
            count += 1
            print("Попробуйте ещё раз")
            sleep(0.5)

# Основная часть программы
if __name__ == "__main__":
    # Создаем канал связи между процессами
    first_part_of_pipe, second_part_of_pipe = Pipe()
    # Запускаем процесс, который отслеживает время подписки
    p1 = Process(target=subscription, args=(time, first_part_of_pipe), daemon=True)
    p1.start()
    # Запускаем игру
    game(num, second_part_of_pipe)