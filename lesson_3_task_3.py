"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib
import re
from uuid import uuid4


def hash_string(some_string):
    hash_part_string = hashlib.sha256(some_string.encode()).hexdigest()
    return hash_part_string


string = 'papa'
substrings = set()
for i in range(0, len(string)+1):
    for j in range(i+1, len(string)+1):
        substring = string[i:j]
        if substring != string:
            substrings.add(hash_string(substring))
print(f'В строке {string} - {len(substrings)} подстрок')
