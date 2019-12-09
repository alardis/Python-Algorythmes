# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


import random


size = 10
unsorted_list = [random.randint(-size, size) for _ in range(size)]
print(f'Исходный массив: {unsorted_list}')


# реализуем алгоритм сортировки пузырьком
def sort_bubble(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        n += 1
    return my_list


# реализуем алгоритм сортировки пузырьком с улучшениями
# алгоритм запоминает, был ли какой-то обмен при текущем обходе. если обмена не было, цикл вновь не стартует. значит,
# все и так уже отсортировано. вполне себе улучшение.
def sort_bubble_2(my_list):
    n = 1
    swap = True
    while n < len(my_list) and swap:
        swap = False
        for i in range(len(my_list) - n):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swap = True
        n += 1
    return my_list


# работа с функцией
print(f'Отсортированный массив: {sort_bubble_2(unsorted_list)}')

