# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

import hashlib


def sub_search(base_string: str, sub_string: str, logs=None) -> (list, int):
    assert len(base_string) > 0 and len(sub_string) > 0, 'Строки не могут быть пустыми'
    assert len(base_string) >= len(sub_string), 'Подстрока длиннее строки'

    if not logs:
        logs = []

    len_sub_string = len(sub_string)
    h_sub_string = hashlib.sha1(sub_string.encode('utf-8')).hexdigest()

    for i in range(len(base_string) - len_sub_string + 1):
        if h_sub_string == hashlib.sha1(base_string[i:i + len_sub_string].encode('utf-8')).hexdigest():
            if base_string[i:i + len_sub_string] == sub_string and base_string[i:i + len_sub_string] != base_string:
                logs.append(f'Подстрока найдена в позиции {i}')

    return logs, len(logs)


s = input('Введите строку для поиска, в ней будем искать:\n')
sub_s = input('Введите подстроку, которую будем искать в строке:\n')

search_results, count = sub_search(s, sub_s)
if len(search_results) > 0:
    print(f'Подстрока всего встречается {count} раз. И вот они:')
    for record in search_results:
        print(record)
else:
    print('Подстроки найдено не было')

