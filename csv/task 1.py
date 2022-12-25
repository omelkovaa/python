"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv
with open ('Task1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(Task1.csv)