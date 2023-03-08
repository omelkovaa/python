"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
from multiprocessing import Process, Pipe


def money(conn, val):
    conn.send(int(val) * 75)
    conn.close()


if __name__ == '__main__':
    val = input('Введите кол-во валюты: ')
    while val != 'off':
        first_conn, sin_conn = Pipe()
        p = Process(target=money, args=(sin_conn, val))

        p.start()
        print(first_conn.recv())
        p.join()
        val = input('Введите количество валюты: ')