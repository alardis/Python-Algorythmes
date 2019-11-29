# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — с помощью классического алгоритма.


# n = int(input('До какого числа получить простые числа:  '))


def sieve(count):
    sieve_list = [2, ]
    number = 3

    # взять цикл while, продлевать цифровой ряд каждый раз, пока оно надо
    while len(sieve_list) < count:
        add_flag = True
        for item in sieve_list:
            if number % item == 0:
                add_flag = False
                break
        if add_flag:
            sieve_list.append(number)
        number += 1

    # print(sieve_list)
    # print(f'Нашли простое {count} число -- {sieve_list[count-1]}')


def prime(count):
    prime_list = [2, ]

    number = 3
    while len(prime_list) < count:
        d = 2
        while number % d != 0:
            d += 1
        if number == d:
            prime_list.append(number)
        number += 1

    # print(prime_list)
    # print(f'Нашли простое {count} число -- {prime_list[count - 1]}')


# sieve(n)
# 100 loops, best of 5: 862 usec per loop  ---  100
# 100 loops, best of 5: 83.5 msec per loop ---  1000

# prime(n)
# 100 loops, best of 5: 4.26 msec per loop ---  100
# 100 loops, best of 5: 812 msec per loop ---  1000

# ВЫВОД: однозначно Эратосфен отлично придумал.
