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
import cProfile


def get_max_from_min(size_x, size_y):
    size_hor = size_x
    size_vert = size_y
    matrix = [[random.randint(0, 20) for _ in range(size_hor)] for _ in range(size_vert)]
    min_list = []

    for i in range(len(matrix[0])):
        min_item = matrix[0][i]
        for j in range(len(matrix)):
            if matrix[j][i] < min_item:
                min_item = matrix[j][i]
        min_list.append(min_item)

    max_min = 0
    for i in min_list:
        if i > max_min:
            max_min = i
    # return max_min


def get_max_from_min_1(size_x, size_y):
    matrix = [[random.randint(0, 20) for _ in range(size_x)] for _ in range(size_y)]
    min_list = []

    for i in range(len(matrix[0])):
        col_list = [matrix[j][i] for j in range(len(matrix))]
        min_item = min(col_list)
        min_list.append(min_item)

    max_min = max(min_list)
    # return max_min


def get_max_from_min_2(size_x, size_y):
    matrix = [[random.randint(0, 20) for _ in range(size_x)] for _ in range(size_y)]
    min_list = []

    [(lambda i: min_list.append(min([matrix[j][i] for j in range(len(matrix))])))(i) for i in range(len(matrix[0]))]

    max_min = max(min_list)
    # return max_min