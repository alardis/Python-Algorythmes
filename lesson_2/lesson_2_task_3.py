# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


number = input('Введите целое число, а мы выведем его цифры наоборот:\n')

try:
    buffer = int(number)
    result = ''
    while buffer / 10 > 0:
        result += str(buffer % 10)
        buffer = buffer // 10

    print(result)
except ValueError:
    print('Проверьте ввод! Что-то пошло не так')

