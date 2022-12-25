"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv

with open('Task1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], row[1], ':', {row[2]: row[3]})