# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


# ввод пользовательской информации
print('Мы определим расстояние между введенными буквами')
letter1 = input('Введите первую букву:\n')
letter2 = input('Введите вторую букву:\n')

# нас интересует не код, а номер буквы в алфавите
letter1_number = ord(letter1) - 96
letter2_number = ord(letter2) - 96

# нам все равно, которое из значений больше. нас интересует только расстояние между двумя точками на числовой прямой,
# не включая ни одно из этих значений
result = abs(letter1_number - letter2_number) - 1

# Вывод результатов
print(f'Ваша буква _{letter1}_ стоит на {letter1_number}, а буква _{letter2}_ -- на {letter2_number}')
print(f'Между вашими буквами расстояние в -- {result}')
