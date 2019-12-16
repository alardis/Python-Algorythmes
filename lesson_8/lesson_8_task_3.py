# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


import random


def get_graph(n_edges):
    my_graph = {}
    for node in range(n_edges):
        node_list = []
        for node_second in range(n_edges):
            if node != node_second:
                try:
                    if my_graph[node_second][node] == 1:
                        node_list.append(1) if random.random() > 0.7 else node_list.append(0)
                except KeyError:
                    node_list.append(1)
            else:
                node_list.append(0)
        my_graph.update({node: node_list})

    for key, value in my_graph.items():
        print(f'{key:3}:  {value}')
    print()
    print('*' * 50)
    return my_graph


def dfs(my_graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(visited)
    available_nodes = set()
    for i, vertex in enumerate(my_graph[start]):
        if vertex == 1:
            available_nodes.add(i)
    for next in set(available_nodes) - visited:
        dfs(my_graph, next, visited)
    return visited


graph = get_graph(4)

dfs(graph, 0)
