"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""

import sys

input_ = sys.argv

if not '--name' in input_:
    print('Привет мир')
else:
    name = ''
    for i in input_:
        if i == '--name':
            name = input_[input_.index(i) + 1]
    print(f'Привет, {name}')





