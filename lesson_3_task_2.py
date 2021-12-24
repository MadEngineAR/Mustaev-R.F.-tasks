"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
# ДЛЯ РЕШЕНИЯ ИЧПОЛЬЗОВАЛ УЧЕБНУЮ Б.Д. 'VK' ИЗ КУРСА MYSQL. В КАЧЕСТВЕ SALT ВЗЯЛ EMAIL(UNIQUE). ДЕЛАЮ ВЫБОРКУ ИЗ
# VK. ЕСЛИ SELECT ВОЗВРАЩАЕТ ХЭШ, ИДЕТ СРАВНЕНИЯ С ВВЕДЕННЫМ ХЭШЭМ. В ПРОИВНОМ СЛУЧАЕ ИДЕТ ЗАПИСЬ В БД
import hashlib
import mysql.connector


def memorize(func):
    def g(some_email, some_password):
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="ruslan1984", database="vk")
        cursor = myconn.cursor()
        cursor.execute("""SELECT password_hash FROM users where email = %s""", (email,))
        result_db = str(cursor.fetchone())
        result_python = func(some_email, some_password)
        if result_db != 'None':
            result_db_correct = result_db.split("'")[1]
            if result_db_correct != result_python:
                print(f'Вы ввели не правильный пароль!')
                exit(1)
            print(f'Правильный пароль!')
            return result_db_correct
        else:
            print('Данного пользвателя не существует. Запись в базу данных')
            cur = myconn.cursor()
            cur.execute("""
                        INSERT INTO users (firstname, lastname, email, password_hash, phone, is_deleted)
                        VALUES
                            (%s, %s, %s, %s, %s, %s)
                    """, ('None', 'None', email, result_python, 0, 0))
            myconn.commit()
            return result_python

    return g


@memorize
def pass_hash(some_email, some_password):
    salt = some_email
    hash_pass = hashlib.sha256(salt.encode() + some_password.encode()).hexdigest()
    print(f'HASH введенного пароля {hash_pass}')
    return hash_pass


print(f'Введите email')
email = input()
print(f'Введите пароль')
password = input()
pass_hash(email, password)
