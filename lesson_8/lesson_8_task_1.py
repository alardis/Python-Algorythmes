# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


import random
from collections import namedtuple


# Найдем, сколько именно друзей было
n_friends = random.randint(2, 20)

# начнем строить граф. поскольку каждый жмет руку другому, направления тут нет. то есть, граф неориентированный
# Этот граф будет для красоты
g_handshake = {}

for node in range(n_friends):
    node_list = []
    for node_second in range(n_friends):
        if node != node_second:
            node_list.append(1)
        else:
            node_list.append(0)
    g_handshake.update({node: node_list})

for key, value in g_handshake.items():
    print(f'{key:3}:  {value}')
print()
print('*' * 50)

print(f'А вот этот -- для дела')
g_handshake_2 = []
count = 0

for node in range(n_friends):
    for node_second in range(n_friends):
        if node != node_second:
            if (node, node_second) not in g_handshake_2 and (node_second, node) not in g_handshake_2:
                g_handshake_2.append((node, node_second))
                count += 1

print(g_handshake_2)
print(f'Всего руки пожимались {count} раз')




