# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
# додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
# У граф додано ваги ребер, програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі.

import networkx as nx
from task1 import G
import random

def add_weights_to_graph(graph: nx.Graph) -> None:
    for edge in graph.edges():
        graph[edge[0]][edge[1]]['weight'] = round(random.uniform(1, 3), 2)
    
    transfers = [
        ('Театральна', 'Золоті ворота'),
        ('Хрещатик', 'Майдан Незалежності'),
        ('Площа Льва Толстого', 'Палац спорту')
    ]
    for station1, station2 in transfers:
        graph[station1][station2]['weight'] = round(random.uniform(3, 5), 2)

def dijkstra(graph: nx.Graph, start: str) -> dict:
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

def print_path_info(start: str, end: str, distance: float) -> None:
    print(f"\nШлях від {start} до {end}:")
    print(f"Загальна відстань: {distance:.2f} км")

if __name__ == "__main__":
    add_weights_to_graph(G)
    
    test_stations = [
        'Академмістечко',
        'Хрещатик',
        'Героїв Дніпра',
        'Червоний хутір'
    ]
    
    print("Найкоротші шляхи за алгоритмом Дейкстри:\n")
    
    for start in test_stations:
        distances = dijkstra(G, start)
        print(f'distances from {start}:', distances)
        
        for end in test_stations:
            if start != end:
                print_path_info(start, end, distances[end])



