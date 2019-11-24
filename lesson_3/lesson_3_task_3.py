# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random


my_list = [random.randint(0, 20) for _ in range(20)]
print(f'Мы создали список из неотрицательных целых чисел:\n{my_list}\nИ теперь поменяем местами минимум и максимум\n')

min_i = 0
min_num = 0
max_i = 0
max_num = 0

for i, num in enumerate(my_list):
    if num < my_list[min_i]:
        min_i = i
    if num > my_list[max_i]:
        max_i = i

spam = my_list[min_i]
my_list[min_i] = my_list[max_i]
my_list[max_i] = spam
print(f'Минимальный элемент стоит на позиции {min_i} -- {my_list[min_i]}')
print(f'Максимальный элемент стоит на позиции {max_i} -- {my_list[max_i]}')

print(f'Вот и поменяли. Получилось:\n{my_list}')
