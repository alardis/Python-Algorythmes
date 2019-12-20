# Закодируйте любую строку по алгоритму Хаффмана.


from copy import deepcopy


class MyNode:
    def __init__(self, left=None, right=None, value=None, weight=0):
        self.left = left
        self.right = right
        self.value = value
        self.weight = weight

    def __str__(self):
        return f'{self.value}({self.weight})'


def huffman_encode(s):

    symbol_dict = {}
    # сперва составим карту символов
    for letter in s:
        if letter not in symbol_dict.keys():
            symbol_dict[letter] = 1
        else:
            symbol_dict[letter] += 1

    symbol_dict = {k: v for k, v in sorted(symbol_dict.items(), key=lambda item: item[1], reverse=True)}
    print(symbol_dict)

    # начинаем развлекаться с формированием дерева
    while len(symbol_dict) > 1:
        # связываем в ветку дерева два левых значения в отсортированном словаре
        first = symbol_dict.popitem()
        second = symbol_dict.popitem()
        node = MyNode(left=first[0], right=second[0], weight=first[1] + second[1], value=f'+{first[0]}+{second[0]}+')
        print(f'Создаем вершину с ветвями {node.left} и {node.right}, вес -- {node.weight}')
        symbol_dict.update({node: node.weight})
        symbol_dict = {k: v for k, v in sorted(symbol_dict.items(), key=lambda item: item[1], reverse=True)}

    # возможно, здесь мы захотим убедиться, что дерево у нас и вправду есть
    # if len(symbol_dict) == 1:
    #     print(symbol_dict.popitem()[0])

    # время закодировать строку по дереву
    encoded_string = ''
    node_base = symbol_dict.popitem()[0]
    for letter in s:
        letter_encoded = False
        letter_code = ''
        node = deepcopy(node_base)
        while not letter_encoded:
            if letter in str(node.left) and letter != str(node.left):
                letter_code = f'{letter_code}{"0"}'
                node = node.left
            elif letter in str(node.right) and letter != str(node.right):
                letter_code = f'{letter_code}{"1"}'
                node = node.right
            elif letter in str(node.left) and letter == str(node.left):
                letter_code = f'{letter_code}{"0"}'
                letter_encoded = True
            elif letter in str(node.right) and letter == str(node.right):
                letter_code = f'{letter_code}{"1"}'
                letter_encoded = True
        encoded_string = f'{encoded_string}{letter_code} '

    print(f'Закодированная строка {s}:\n{encoded_string}')


string_to_encode = 'beep boop beer!'
huffman_encode(string_to_encode)
