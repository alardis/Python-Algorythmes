# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
#       трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
#       для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

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


# cProfile.run('get_max_from_min(5, 5)')
# result = get_max_from_min(400, 200)

# (venv) D:\YandexDisk\РАБОТА\Python\Python-Algorythmes\lesson_4>
# python -m timeit -n 100 -s "import lesson_4_task_1_0" "lesson_4_task_1_0.get_max_from_min(200,200)"

# GET_MAX_FROM_MIN() --- наблюдается линейая зависимость
# 100 loops, best of 5: 29.9 usec per loop   ---- 5, 5
# 100 loops, best of 5: 2.75 msec per loop   ---- 50, 50
# 100 loops, best of 5: 10.8 msec per loop   ---- 100, 100
# 100 loops, best of 5: 44.1 msec per loop   ---- 200, 200
# 100 loops, best of 5: 90.4 msec per loop   ---- 400, 200


# GET_MAX_FROM_MIN_1()

