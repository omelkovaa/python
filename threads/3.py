"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import time
from multiprocessing import Process


def hurry():
    while True:
        print('Вводите быстрее')
        time.sleep(3)

process = Process(daemon=True, target=hurry)
process.start()
password = '123456'
user_pswd = input('Code: \n')
if user_pswd == password:
    print('Бомба разминирована')
else:
    print('Вы взорвались')