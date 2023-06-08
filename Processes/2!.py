"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""


import multiprocessing

def calculate_room_area(width, length, height, result_queue):
    area = 2 * (width + length) * height
    result_queue.put(area)

def calculate_paint_consumption(area, result_queue):
    consumption = area * 5
    result_queue.put(consumption)


if __name__ == '__main__':
    # Пример использования функции и записи в файл
    width = 5
    length = 6
    height = 3
    file_name = "room_details.txt"

    result_queue = multiprocessing.Queue()

    area_process = multiprocessing.Process(target=calculate_room_area, args=(width, length, height, result_queue))
    area_process.start()
    area_process.join()
    area = result_queue.get()

    consumption_process = multiprocessing.Process(target=calculate_paint_consumption, args=(area, result_queue))
    consumption_process.start()
    consumption_process.join()
    consumption = result_queue.get()

    with open(file_name, 'w') as file:
        file.write(f"Ширина комнаты: {width} м\n")
        file.write(f"Длина комнаты: {length} м\n")
        file.write(f"Высота комнаты: {height} м\n")
        file.write(f"Площадь стен комнаты: {area} кв.м\n")
        file.write(f"Расход краски (5 л/кв.м): {consumption} л\n")



    print("Данные о комнате записаны в файл.")



# Функция calculate_room_area принимает параметры width, length, height и result_queue.
# Она вычисляет площадь стен комнаты и записывает ее в очередь result_queue.
#
# Функция calculate_paint_consumption принимает параметры area и result_queue.
# Она вычисляет расход краски на стены комнаты и записывает его в очередь result_queue.
