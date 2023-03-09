"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

from queue import Queue
from threading import Thread
from time import sleep

queue = Queue()

for i in ['omelkova', 'morgacheva']:
    queue.put(i)


def input_cons(queue):
    while True:
        name = input('Фамилия: ')
        while name != 'off':
            queue.put(name)
            name = input('Фамилия: ')


def expelled(queue):
    while queue:
        if not queue.empty():
            print(f'\n{queue.get()} отчислен.\n')


def main():
    input_thread = Thread(target=input_cons, args=(queue,))
    input_thread.start()

    expelled_thread = Thread(target=expelled, args=(queue,), daemon=True)
    expelled_thread.start()


if __name__ == '__main__':
    main()