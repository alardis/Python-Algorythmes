# Закодируйте любую строку по алгоритму Хаффмана.


class MyNode:
    def __init__(self, left=None, right=None, value=None, weight=0):
        self.left = left
        self.right = right
        self.value = value
        self.weight = weight

    def __str__(self, level=0, ret=None):
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

    # print(symbol_dict)
    if len(symbol_dict) == 1:
        print(symbol_dict.popitem()[0])


string_to_encode = 'beep boop beer!'
huffman_encode(string_to_encode)
