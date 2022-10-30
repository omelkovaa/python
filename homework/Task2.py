"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""

from random import randint

number = int(input('Число участников сборной: '))
cup1 = randint(1, number)
cup2 = randint(1, number)
while cup1 == cup2:
    cup2 = randint(1, number)
print(cup1, '-', cup2)