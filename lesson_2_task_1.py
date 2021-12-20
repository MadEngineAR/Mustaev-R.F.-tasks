"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя."""


def calc():
    try:
        print(f'Введите арифметическую операцию. Или "0" для выхода')
        operation = input()
        if operation  not in ['0', '+', '-', '*', '/']:
            raise ValueError("Несоответствующее значение операции повторите ввод")
        if operation == '0':
            message = 'Программа заврешена'
            print(message)
            return message
        try:
            print(f'Введите число 1')
            a = int(input())
        except ValueError:
            print(f'Введите число 1')
            a = int(input())
        try:
            print(f'Введите число 2')
            b = int(input())
        except ValueError:
            print(f'Введите число')
            b = int(input())
        if operation == '+':
            return print(f'Сумма =  {a + b}'), calc()

        elif operation == '-':
            return print(f'Разность =  {a - b}'), calc()
        elif operation == '*':
            return print(f'Произведение =  {a * b}'), calc()
        elif operation == '/':
                return print(f'Частное =  {a / b}'), calc()
        elif operation == '/' and b == 0:
                print(f'На ноль делить нельзя'), calc
    except ValueError:
        print("Несоответствующее значение операции повторите ввод")
        return calc()
    except ZeroDivisionError:
        print(f'На ноль делить нельзя')
        return calc()

print(calc())


