# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random

size_hor = 5
size_vert = 5
matrix = [[random.randint(0, 20) for _ in range(size_hor)] for _ in range(size_vert)]
min_list = []

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

for i in range(len(matrix[0])):
    min_item = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min_item:
            min_item = matrix[j][i]
    min_list.append(min_item)

print('-' * len(matrix[0]) * 4)

for item in min_list:
    print(f'{item:>4}', end='')
print()


max_min = 0
for i in min_list:
    if i > max_min:
        max_min = i

print(f'\nМаксимальный элемент среди миниальных в столбцах матрицы: {max_min}')