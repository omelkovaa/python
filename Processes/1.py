"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing


def even():
    even_sum = 0
    for numb in range(1, 1000001):
        if numb % 2 == 0:
            even_sum += numb
    print(even_sum)


def odd():
    odd_sum = 0
    for numb in range(1, 1000001):
        if numb % 2 != 0:
            odd_sum += numb
    print(odd_sum)


def main():
    proc1 = multiprocessing.Process(target=even)
    proc2 = multiprocessing.Process(target=odd)

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()


if __name__ == '__main__':
    main()