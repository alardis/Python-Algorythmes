# Определить, какое число в массиве встречается чаще всего.


import random


numbers = [random.randint(0, 20) for _ in range(20)]
print(f'Найдем, какое число чаще всего встречается в массиве:\n{numbers}')

numbers_set = set(numbers)

most_common = None
most_common_count = 0

for item in numbers_set:
    local_count = numbers.count(item)
    if most_common_count < local_count:
        most_common_count = local_count
        most_common = item

print(f'Число {most_common} встречается раз: {most_common_count}')
