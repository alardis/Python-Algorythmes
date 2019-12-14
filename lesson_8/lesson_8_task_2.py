# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.


import random
import networkx as nx
import numpy as np


# функция генерации графа
def get_graph(n_edges):
    my_graph = {}
    for node in range(n_edges):
        node_list = []
        for node_second in range(n_edges):
            if node != node_second:
                node_list.append(random.randint(0, n_edges))
            else:
                node_list.append(0)
        my_graph.update({node: node_list})

    for key, value in my_graph.items():
        print(f'{key:3}:  {value}')
    print()
    print('*' * 50)
    return my_graph


# реализация алгоритма Дейкстры
def deykstra_ench(my_graph, start):
    length = len(my_graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    route_dict = {}
    route_dict.update({start: 'start'})

    while min_cost < float('inf'):
        is_visited[start] = True

        route_list = []
        for i, vertex in enumerate(my_graph[start]):
            if vertex != 0 and not is_visited[i]:
                print(f'Рассматриваем вершину {i}, расстояние до нее -- {vertex}')
                route_list.append(i)
                if cost[i] > vertex + cost[start]:
                    print(f'Прошлое расстояние {cost[i]}, нынешнее -- {vertex + cost[start]}')
                    print(f'route_list: {route_list}')
                    route_dict.update({i: route_list})
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, route_dict


point = int(input('Из какой вершины идти:  '))
n = random.randint(2, 20)
print('\n' + '*' * 50)
graph = get_graph(n)
routes = deykstra_ench(graph, point)
print(routes)

# визуализация графа
g_vis = nx.from_dict_of_lists(graph)
nx.draw(g_vis)
