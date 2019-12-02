# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque


dec_to_hex = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
              '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

hex_to_dec = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
              'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}


def add_hex(one: list, two: list):
    one_dec = 0
    for num, item in enumerate(one):
        one_dec += int(hex_to_dec[item]) * (16 ** (len(one) - num - 1))
    print(f'Из числа {one} получили -- {one_dec}')

    two_dec = 0
    for num, item in enumerate(two):
        two_dec += int(hex_to_dec[item]) * (16 ** (len(two) - num - 1))
    print(f'Из числа {two} получили -- {two_dec}')

    result_dec = one_dec + two_dec
    result_hex = deque([])
    while result_dec != 0:
        result_hex.appendleft(dec_to_hex[str(result_dec % 16)])
        result_dec = result_dec // 16
    result_hex = list(result_hex)
    print(f'Сумма получилась: {result_hex}')


def mul_hex(one: list, two: list):
    one_dec = 0
    for num, item in enumerate(one):
        one_dec += int(hex_to_dec[item]) * (16 ** (len(one) - num - 1))
    print(f'Из числа {one} получили -- {one_dec}')

    two_dec = 0
    for num, item in enumerate(two):
        two_dec += int(hex_to_dec[item]) * (16 ** (len(two) - num - 1))
    print(f'Из числа {two} получили -- {two_dec}')

    result_dec = one_dec * two_dec
    result_hex = deque([])
    while result_dec != 0:
        result_hex.appendleft(dec_to_hex[str(result_dec % 16)])
        result_dec = result_dec // 16
    result_hex = list(result_hex)
    print(f'Произведение получилось: {result_hex}')


one_list = list(input('Введите первое число в шестнадцатиричной форме:\n'))
two_list = list(input('Введите второе число в шестнадцатиричной форме:\n'))

add_hex(one_list, two_list)
mul_hex(one_list, two_list)