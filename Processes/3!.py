"""
Напишите функцию которая через канал обмена возвращает количество валюты
которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой
в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""

import multiprocessing
import time

def calculate_currency_amount(money, conn):
    exchange_rate = 75
    currency_amount = money // exchange_rate
    conn.send(currency_amount)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    amount_1 = 1000
    amount_2 = 5000

    process = multiprocessing.Process(target=calculate_currency_amount, args=(amount_1, child_conn))
    process.start()
    time.sleep(0.5)
    print(f"Количество валюты за {amount_1} сум: {parent_conn.recv()}")

    process = multiprocessing.Process(target=calculate_currency_amount, args=(amount_2, child_conn))
    process.start()
    time.sleep(0.5)
    print(f"Количество валюты за {amount_2} сум: {parent_conn.recv()}")