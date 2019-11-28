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


def get_max_from_min_2(size_x, size_y):
    matrix = [[random.randint(0, 20) for _ in range(size_x)] for _ in range(size_y)]
    min_list = []

    [(lambda i: min_list.append(min([matrix[j][i] for j in range(len(matrix))])))(i) for i in range(len(matrix[0]))]

    max_min = max(min_list)
    # return max_min


cProfile.run('get_max_from_min_2(400, 200)')
# result = get_max_from_min(400, 200)

# (venv) D:\YandexDisk\РАБОТА\Python\Python-Algorythmes\lesson_4>
# python -m timeit -n 100 -s "import lesson_4_task_1_0" "lesson_4_task_1_0.get_max_from_min(200,200)"

# ------------------------------------------------------
# GET_MAX_FROM_MIN() --- наблюдается линейная зависимость
# ------------------------------------------------------
# 100 loops, best of 5: 29.9 usec per loop   ---- 5, 5
# 100 loops, best of 5: 2.75 msec per loop   ---- 50, 50
# 100 loops, best of 5: 10.8 msec per loop   ---- 100, 100
# 100 loops, best of 5: 44.1 msec per loop   ---- 200, 200
# 100 loops, best of 5: 90.4 msec per loop   ---- 400, 200

# cProfile.run('get_max_from_min(5, 5)')
# 151 function calls in 0.001 seconds
# по 25 вызовов random-функций

# cProfile.run('get_max_from_min(50, 50)')
# 13943 function calls in 0.005 seconds
# по 2500 вызовов random-функций

# cProfile.run('get_max_from_min(100, 100)')
# 55505 function calls in 0.017 seconds
# по 10000 вызовов random-функций

# cProfile.run('get_max_from_min(200, 200)')
# 221230 function calls in 0.071 seconds
# по 40000 вызовов random-функций

# cProfile.run('get_max_from_min(400, 200)')
# 443001 function calls in 0.138 seconds
# 80000 вызовов random-функций


# ------------------------------------------------------
# GET_MAX_FROM_MIN_1() --- наблюдается линейная зависимость
# ------------------------------------------------------
# 100 loops, best of 5: 31.8 usec per loop   ---- 5, 5
# 100 loops, best of 5: 2.78 msec per loop   ---- 50, 50
# 100 loops, best of 5: 11.7 msec per loop   ---- 100, 100
# 100 loops, best of 5: 45.8 msec per loop   ---- 200, 200
# 100 loops, best of 5: 92.9 msec per loop   ---- 400, 200

# cProfile.run('get_max_from_min_1(5, 5)')
# 171 function calls in 0.000 seconds

# cProfile.run('get_max_from_min_1(50, 50)')
# 14079 function calls in 0.005 seconds

# cProfile.run('get_max_from_min_1(100, 100)')
# 55580 function calls in 0.017 seconds

# cProfile.run('get_max_from_min_1(200, 200)')
# 221768 function calls in 0.069 seconds

# cProfile.run('get_max_from_min_1(400, 200)')
# 443428 function calls in 0.140 seconds


# ------------------------------------------------------
# GET_MAX_FROM_MIN_2() --- наблюдается линейная зависимость
# ------------------------------------------------------
# 100 loops, best of 5: 33.6 usec per loop   ---- 5, 5
# 100 loops, best of 5: 2.87 msec per loop   ---- 50, 50
# 100 loops, best of 5: 11.7 msec per loop   ---- 100, 100
# 100 loops, best of 5: 47.5 msec per loop   ---- 200, 200
# 100 loops, best of 5: 93.4 msec per loop   ---- 400, 200

# cProfile.run('get_max_from_min_2(5, 5)')
# 176 function calls in 0.000 seconds

# cProfile.run('get_max_from_min_2(50, 50)')
# 14019 function calls in 0.004 seconds

# cProfile.run('get_max_from_min_2(100, 100)')
# 55525 function calls in 0.017 seconds

# cProfile.run('get_max_from_min_2(200, 200)')
# 221746 function calls in 0.071 seconds

# cProfile.run('get_max_from_min_2(400, 200)')
# 442981 function calls in 0.136 seconds


# ------------------------------------------------------
# ВЫВОД: будем использовать третий алгоритм, поскольку по времени он отрабатывает за столько же, однако использует
#           меньше переменных, что позитивно сказывается на затраченной памяти.
# ------------------------------------------------------