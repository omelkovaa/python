"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""

import os
import shutil

path = input("Введите путь к папке: ")
name = input("Введите имя папки: ")

if not os.path.exists(path):
    os.makedirs(path)
    print("Папка создана")