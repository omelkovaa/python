"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
from multiprocessing import Process

file_name = "New.txt"


def write():
    global file_name
    length = 4
    width = 4
    height = 4
    result = (length * height * 2) + (width * height * 2)
    with open(f"{file_name}", "w+") as f:
        f.write(str(result) + "\n")
        pass


def read():
    global file_name
    with open(f"{file_name}", "r") as f:
        x = f.read()
    with open(f"{file_name}", "a+") as file:
        file.write(f"Количество краски для данного помещения {int(x) * 5}")


if __name__ == "__main__":
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p1.join()
    p2.start()