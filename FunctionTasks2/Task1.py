"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def task1(parameter1='ok', parameter2=1, parameter3=[1]):
    if parameter1 and parameter2 and parameter3:
        print(parameter1, parameter2, parameter3)



