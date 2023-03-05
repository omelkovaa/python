""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os
os.makedirs(r"/Users/om.anny/Desktop/task4")
with open("answer.txt", "w") as f:
    f.write("я выполнил задание")
