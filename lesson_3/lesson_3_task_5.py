# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random


my_list = [random.randint(-10, 10) for _ in range(10)]

my_max = my_list[0]
for num in my_list:
    if 0 > num > my_max:
        my_max = num

print(f'Мы работаем со списком:\n{my_list}\nИ ищем в нем максимальное отрицательное число')
print(f'Мы нашли вот это число: {my_max}')
