# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))
c = int(input('Введите третье число:\n'))

mean_num = None

if a > b:
    if a > c:
        if b > c:
            mean_num = b
        else:
            mean_num = c
    else:
        mean_num = a
else:
    if b > c:
        if a > c:
            mean_num = a
        else:
            mean_num = c
    else:
        mean_num = b

print(f'Среднее число из введенных -- {mean_num}')