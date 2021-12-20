"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def nums_sum_signed(n, n2=1, summ=float(1), count=2):
    if n == 1:
        return f'Сумма {n1} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... ' \
               f'= {summ}'
    elif count % 2 == 0:
        n = n - 1
        n2 = n2 * 2
        summ = summ - 1 / n2
        return nums_sum_signed(n, n2, summ, count=count + 1)
    else:
        n = n - 1
        n2 = n2 * 2
        summ = summ + 1 / n2
        return nums_sum_signed(n, n2, summ, count=count + 1)


try:
    print(f'Введите число')
    n1 = int(input())
except ValueError:
    print(f'Введите число')
    n1 = int(input())

print(nums_sum_signed(n1))
