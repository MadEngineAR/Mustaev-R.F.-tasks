"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

# СОЗДАЛ В MYSQL БД URL_CASH.
import hashlib
import mysql.connector
from uuid import uuid4


def memorize(func):
    def g(some_url):
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="ruslan1984", database="cash")
        cursor = myconn.cursor()
        cursor.execute("""SELECT hash FROM url_cash where url = %s""", (url,))
        result_db = str(cursor.fetchone())
        result_python = func(some_url)
        if result_db != 'None':
            result_db_correct = result_db.split("'")[1]
            return result_db_correct
        else:
            print('Данного сайта в cash не существует. Запись в базу данных')
            cur = myconn.cursor()
            cur.execute("""
                        INSERT INTO url_cash (url,hash)
                        VALUES
                            (%s, %s)
                    """, (url, result_python))
            myconn.commit()
            return result_python
    return g


@memorize
def url_hash(some_url):
    salt = uuid4().hex
    hash_url= hashlib.sha256(salt.encode() + some_url.encode()).hexdigest()
    print(f'HASH введенного URL {hash_url}')
    return hash_url


print(f'Введите URL')
# ВВОДИЛ https://ru.wikipedia.org/wiki/URL
url = input()
url_hash(url)
