"""
Задание 1.
Реализуйте:
a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.
b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.
ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

# п.A - Использовал perf_counter. Если делать по аналогии с уроком 1 start_val = time.time(), time_val = 0.
# И не понятно то ли bug, то ли нет. Cписок заполняется быстрее. Для ключей словаря производится хэширование,
# на что тоже затрачивается время
import random
import time


# п.A,B
def time_of_function(func):
    def time_total(*args):
        start_val = time.perf_counter_ns()
        obj = func(*args)
        end_val = time.perf_counter_ns()
        time_val = end_val - start_val
        print(f'{func.__qualname__} заняла := {time_val}')
        return obj
    return time_total


# п.A
@time_of_function
def list_insert(n1):                               # O(N)
    list1 = [num for num in range(n1)]
    return list1


@time_of_function
def dict_insert(n1):                                # O(N)
    dict1 = {num: num + 100 for num in range(n1)}
    return dict1


# п.B. Операции со словарями быстрее, так как данные хрантся в виде хэш таблиц. Отсюда быстрый поиск по совпадающему
# ключу словаря.
@time_of_function
def list_update_el(n2, l1):        # O(1)
    l1[n2] = 'Измененный элемент'  # O(1)
    return l1


@time_of_function
def list_delete_el(n3, l1):        # O(N)
    l1.pop(n3)    # O(N)
    return l1


@time_of_function
def dict_change_el(n4, d1):        # O(1)
    d1[n4] = 'Измененный элемент'  # O(1)
    return d1


@time_of_function
def dict_del_el(n4, d1):           # O(1)
    d1.pop(n4)                    # O(1)
    return d1


n = 5
list_insert(n)
dict_insert(n)
list_update_el(3, list_insert(n))
dict_change_el(3, dict_insert(n))
list_delete_el(3, list_insert(n))
dict_del_el(3, dict_insert(n))
