# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
#   с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

# Оригинальное задание:
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random
import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


def get_max_from_min(size_x, size_y):
    size_hor = size_x
    size_vert = size_y
    matrix = [[random.randint(0, 20) for _ in range(size_hor)] for _ in range(size_vert)]
    show_size(matrix)
    min_list = []

    for i in range(len(matrix[0])):
        min_item = matrix[0][i]
        for j in range(len(matrix)):
            if matrix[j][i] < min_item:
                min_item = matrix[j][i]
        min_list.append(min_item)
    show_size(min_list)
    show_size(min_item)

    max_min = 0
    for i in min_list:
        if i > max_min:
            max_min = i

    show_size(max_min)
    return max_min


def get_max_from_min_1(size_x, size_y):
    matrix = [[random.randint(0, 20) for _ in range(size_x)] for _ in range(size_y)]
    show_size(matrix)
    min_list = []

    for i in range(len(matrix[0])):
        col_list = [matrix[j][i] for j in range(len(matrix))]
        min_item = min(col_list)
        min_list.append(min_item)
        show_size(min_item)
    show_size(min_list)

    max_min = max(min_list)
    show_size(max_min)
    return max_min


def get_max_from_min_2(size_x, size_y):
    matrix = [[random.randint(0, 20) for _ in range(size_x)] for _ in range(size_y)]
    show_size(matrix)
    min_list = []

    show_size([(lambda i: min_list.append(min([matrix[j][i] for j in range(len(matrix))])))(i) for i in range(len(matrix[0]))])

    max_min = max(min_list)
    show_size(min_list)
    show_size(max_min)
    return max_min

print(sys.version, sys.platform)
print(get_max_from_min_1(5, 5))

# Исследование проводилось со следующими параметрами:
# 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] win32

# Исследование первой функции
'''
# *********************************************************************************************************************
# Исследование функции get_max_from_min
# *********************************************************************************************************************
# ---> Затраты памяти для параметров размеров матрицы
#  type = <class 'int'>, size = 28, object = 5
#  type = <class 'int'>, size = 28, object = 5
#  ---> Затраты памяти для матрицы
# type = <class 'list'>, size = 120, object = [[17, 5, 18, 1, 1], [3, 5, 8, 1, 19], [12, 13, 14, 12, 17],
#                                                                           [1, 13, 5, 11, 1], [8, 2, 8, 17, 0]]
# ---> Затраты памяти для первой строки (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [17, 5, 18, 1, 1]
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 1
# ---> Затраты памяти для второй строки (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [3, 5, 8, 1, 19]
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 19
# ---> Затраты памяти для третьей строки (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [12, 13, 14, 12, 17]
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 14
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 17
# ---> Затраты памяти для четвертой строки (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [1, 13, 5, 11, 1]
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 1
# ---> Затраты памяти для пятой строки (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [8, 2, 8, 17, 0]
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 24, object = 0
# ---> Затраты памяти для списка сумм столбцов (с учетом "веса" самого содерживого ячеек -- 260 байт)
#  type = <class 'list'>, size = 120, object = [1, 2, 5, 1, 0]
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 5
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'int'>, size = 24, object = 0
# ---> Затраты памяти на хранение целевого результата работы функции
#  type = <class 'int'>, size = 28, object = 10

# Итого в процессе осуществления функции затрачивается порядка __1792 байта__. В переменных хранится достаточно много
# информации.
'''

# Исследование второй функции -- выбран оптимальным
'''
# *********************************************************************************************************************
# Исследование функции get_max_from_min_1
# *********************************************************************************************************************
# ---> Затраты памяти для матрицы
#  type = <class 'list'>, size = 120, object = [[12, 5, 18, 19, 18], [16, 7, 18, 1, 19], [16, 1, 3, 17, 6],
#                                                                          [20, 13, 8, 12, 15], [3, 1, 6, 6, 6]]
# ---> Затраты памяти для матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [12, 5, 18, 19, 18]
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 19
# 		 type = <class 'int'>, size = 28, object = 18
# ---> Затраты памяти для матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [16, 7, 18, 1, 19]
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 19
# ---> Затраты памяти для матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [16, 1, 3, 17, 6]
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 6
# ---> Затраты памяти для матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [20, 13, 8, 12, 15]
# 		 type = <class 'int'>, size = 28, object = 20
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 15
# ---> Затраты памяти для матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [3, 1, 6, 6, 6]
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 6
# ---> Затраты памяти для хранения промежуточного результата сравнения
#  type = <class 'int'>, size = 28, object = 3
# ---> Затраты памяти для списка сумм столбцов (с учетом "веса" самого содерживого ячеек -- 260 байт)
#  type = <class 'list'>, size = 120, object = [3, 1, 3, 1, 6]
# 	 type = <class 'int'>, size = 28, object = 3
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'int'>, size = 28, object = 3
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'int'>, size = 28, object = 6
# ---> Затраты памяти на хранение целевого результата работы функции
#  type = <class 'int'>, size = 28, object = 6

# Итого на работу функции ушло 1760 байт. Чуть меньше, чем в прошлый раз, но в переменных все еще содержится много 
данных.

# Пожалуй, именно этот вариант можно считать ___оптимальным___. Он занимает меньше памяти, имеет меньше строк кода.

'''

# Исследование третьей функции
'''
# *********************************************************************************************************************
# Исследование функции get_max_from_min_2
# *********************************************************************************************************************
# ---> Затраты памяти для матрицы
# type = <class 'list'>, size = 120, object = [[5, 18, 13, 3, 19], [14, 10, 3, 7, 17], [2, 0, 0, 17, 12],
#                                                                           [8, 20, 12, 10, 7], [2, 10, 11, 17, 16]]
# ---> Затраты памяти для строки матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [5, 18, 13, 3, 19]
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 19
# ---> Затраты памяти для строки матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [14, 10, 3, 7, 17]
# 		 type = <class 'int'>, size = 28, object = 14
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 17
# ---> Затраты памяти для строки матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [2, 0, 0, 17, 12]
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 24, object = 0
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 12
# ---> Затраты памяти для строки матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [8, 20, 12, 10, 7]
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 20
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 7
# ---> Затраты памяти для строки матрицы (с учетом "веса" самого содерживого ячеек -- 260 байт)
# 	 type = <class 'list'>, size = 120, object = [2, 10, 11, 17, 16]
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 17
# 		 type = <class 'int'>, size = 28, object = 16
# ---> Затраты памяти для остатков работы лямбда-функции (с учетом "веса" самого содерживого ячеек -- 200 байт)
#  type = <class 'list'>, size = 120, object = [None, None, None, None, None]
# 	 type = <class 'NoneType'>, size = 16, object = None
# 	 type = <class 'NoneType'>, size = 16, object = None
# 	 type = <class 'NoneType'>, size = 16, object = None
# 	 type = <class 'NoneType'>, size = 16, object = None
# 	 type = <class 'NoneType'>, size = 16, object = None
# ---> Затраты памяти для остатков работы лямбда-функции (с учетом "веса" самого содерживого ячеек -- 252 байт)
#  type = <class 'list'>, size = 120, object = [2, 0, 0, 3, 7]
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'int'>, size = 28, object = 3
# 	 type = <class 'int'>, size = 28, object = 7
# ---> Затраты памяти для остатков работы лямбда-функции
#  type = <class 'int'>, size = 28, object = 7

# Интересно, но на работу функции ушло аж __1900 байт__. Похоже, что лямбда-функция оставляет после себя 
# мусорный список, который тоже занимает место. 

'''

