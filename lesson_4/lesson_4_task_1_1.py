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
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random
from math import inf


def get_min_max_list(size):
    my_list = [random.randint(-10, 10) for _ in range(size)]
    my_max = inf * -1
    for num in my_list:
        if 0 > num > my_max:
            my_max = num


def get_min_max_list_1(size):
    min_list = []
    [(lambda i: i < 0 and min_list.append(i))(random.randint(-10, 10)) for _ in range(size)]
    result = max(min_list)


def get_min_max_list_2(size):
    num = inf * -1
    for _ in range(size):
        i = random.randint(-10, 10)
        if 0 > i > num:
            num = i

# python -m timeit -n 100 -s "import lesson_4_task_1_1" "lesson_4_task_1_1.get_min_max_list_1(100)"
