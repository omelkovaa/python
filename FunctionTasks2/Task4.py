"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def cacluate(*n):
    m = []
    for number in n:
        if number > sum(n) / len(n):
            m.append(number)
    return (sum(n) / len(n), m)


print(cacluate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))