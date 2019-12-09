# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random
import statistics


size_index = 20
my_list = [random.randint(0, size_index) for _ in range(size_index*2 + 1)]
print(f'Исходный массив: {my_list}')

print(f'Медиана списка правильная: {statistics.median(my_list)}')
# находим самый большой и самый малый элементы списка
list_max = max(my_list)
list_min = min(my_list)

list_mean = (list_max + list_min) // 2

# формируем список с правой половиной сортированного массива. не надо их выстраивать,
# они просто должны быть меньше серединного значения
print(list_mean)
list_less = []
list_more = []
my_list_copy = my_list[:]

for item in my_list_copy:
    if list_mean > item:
        # print(f'Рассматриваем число {item}. Сравниваем с {list_mean}')
        list_less.append(item)
    else:
        list_more.append(item)

print(f'Общий размер списка -- {len(my_list)}')
print(f'list_less: {list_less}, размер -- {len(list_less)}')
print(f'list_more: {list_more}, размер -- {len(list_more)}')

# мы не будем сортировать исходный массив. мы отсортируем его кусок. так можно, точно говорю
if len(list_less) > (len(my_list) // 2):
    list_less.sort()
    print(f'Мелиана списка моя: {list_less[len(my_list) // 2]}')
else:
    list_more.sort()
    for item_more in list_more:
        item_mean = min(list_more)
        if len(list_less) < (len(my_list) // 2):
            list_less.append(item_mean)
        else:
            print(f'Мелиана списка моя: {item_mean}')
            break

