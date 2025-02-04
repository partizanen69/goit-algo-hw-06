# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
# Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.
# Програмно реалізовано алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
# Здійснено порівняння результатів алгоритмів для цього графа, пояснено різницю в отриманих шляхах. Обґрунтовано, чому шляхи для алгоритмів саме такі.
# Висновки оформлено у вигляді файлу readme.md домашнього завдання.

import networkx as nx
from task1 import G  # Імпортуємо граф з першого завдання

def find_path_dfs(graph: nx.Graph, start: str, end: str, path: list = None, path_set: set = None) -> list:
    if path is None:
        path = []
        path_set = set()
    path.append(start)
    path_set.add(start)
    
    if start == end:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path_set:
            new_path = find_path_dfs(graph, neighbor, end, path, path_set)
            if new_path:
                return new_path
    
    return None

def find_path_bfs(graph: nx.Graph, start: str, end: str) -> list:
    queue = [(start, [start])]
    visited = {start}
    
    while queue:
        vertex, path = queue.pop(0)
        print('vertex', vertex, 'path', path)
        if vertex == end:
            return path
            
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

if __name__ == "__main__":  
# Тестування алгоритмів на різних маршрутах
    test_routes = [
        ('Академмістечко', 'Хрещатик'),
        ('Героїв Дніпра', 'Палац спорту'),
        ('Сирець', 'Червоний хутір')
    ]

    print("Порівняння шляхів DFS та BFS:\n")

    for start, end in test_routes:
        print(f"\nМаршрут від {start} до {end}:")
        
        dfs_path = find_path_dfs(G, start, end)
        print("DFS шлях:", ' -> '.join(dfs_path))
        print(f"Кількість станцій (DFS): {len(dfs_path)}")
        
        bfs_path = find_path_bfs(G, start, end)
        print("BFS шлях:", ' -> '.join(bfs_path))
        print(f"Кількість станцій (BFS): {len(bfs_path)}")
