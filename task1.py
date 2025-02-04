# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
# info
# 📖 Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.
# Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).
# Створення графу транспортної мережі міста Києва (станції метро)


import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Додавання станцій (вершин) по лініях
red_line = ['Академмістечко', 'Житомирська', 'Святошин', 'Нивки', 'Берестейська', 
           'Шулявська', 'Політехнічна', 'Вокзальна', 'Університет', 'Театральна',
           'Хрещатик', 'Арсенальна', 'Дніпро', 'Гідропарк', 'Лівобережна', 'Дарниця']

blue_line = ['Героїв Дніпра', 'Мінська', 'Оболонь', 'Почайна', 'Тараса Шевченка',
            'Контрактова площа', 'Поштова площа', 'Майдан Незалежності', 'Площа Льва Толстого',
            'Олімпійська', 'Палац Україна', 'Либідська', 'Деміївська', 'Голосіївська', 'Васильківська']

green_line = ['Сирець', 'Дорогожичі', 'Лук\'янівська', 'Золоті ворота', 'Палац спорту',
             'Кловська', 'Печерська', 'Дружби народів', 'Видубичі', 'Славутич', 'Осокорки',
             'Позняки', 'Харківська', 'Вирлиця', 'Бориспільська', 'Червоний хутір']

# Додавання всіх станцій
G.add_nodes_from(red_line)
G.add_nodes_from(blue_line)
G.add_nodes_from(green_line)

# Додавання з'єднань між станціями на червоній лінії
for i in range(len(red_line)-1):
    G.add_edge(red_line[i], red_line[i+1])

# Додавання з'єднань між станціями на синій лінії
for i in range(len(blue_line)-1):
    G.add_edge(blue_line[i], blue_line[i+1])

# Додавання з'єднань між станціями на зеленій лінії
for i in range(len(green_line)-1):
    G.add_edge(green_line[i], green_line[i+1])

# Додавання пересадок між лініями
transfers = [
    ('Театральна', 'Золоті ворота'),
    ('Хрещатик', 'Майдан Незалежності'),
    ('Площа Льва Толстого', 'Палац спорту')
]
G.add_edges_from(transfers)

# Аналіз основних характеристик
print(f"Загальна кількість станцій: {G.number_of_nodes()}")
print(f"Загальна кількість з'єднань: {G.number_of_edges()}")
print("\nСтанції з пересадками (ступінь > 2):")
for station in G.nodes():
    degree = G.degree(station)
    if degree > 2:
        print(f"{station}: {degree} з'єднання")

# Візуалізація графу
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, k=1, iterations=50)

# Малювання ребер
nx.draw_networkx_edges(G, pos)

# Малювання вершин з різними кольорами для різних ліній
nx.draw_networkx_nodes(G, pos, nodelist=red_line, node_color='red', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=blue_line, node_color='blue', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=green_line, node_color='green', node_size=700)

# Додавання підписів станцій
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Схема метро Києва")
plt.axis('off')
plt.show()
