import random
from itertools import permutations

def graph_generator(possibility: float, size, q, r: int) -> set:
    possibility /= 2
    edges = set()
    vertexes = set([v for v in range(size)])

    for combination in permutations(vertexes, 2):
        temp1 = random.random()
        weight = random.randint(q, r)
        if temp1 < possibility:
            current_edge = (combination[0], combination[1], weight)
            edges.add(current_edge)

    matrix = [[0 for i in range(size)] for i in range(size)]
    for edge in edges:
        matrix[edge[0]][edge[1]] = edge[2]

    return matrix

def first_child(i, d, n):
    j = i * d + 1
    if j > n - 1:  # is leaf ?
        return -1
    else:
        return j


def last_child(i, d, n):
    j = first_child(i, d, n)
    if j == -1:
        return -1  # leaf too
    else:
        return min(j + d - 1, n - 1)  # n - 1 if this does not exist


def father(i, d):
    if i == 0:
        return -1  # don't have a father
    else:
        return (i - 1) // d


def min_child(i, d, n):
    kf = first_child(i, d, n)
    if kf == -1:
        return i
    else:
        kl = last_child(i, d, n)
        km = kf
        for j in range(kf + 1, kl + 1):
            if key[j] < key[km]:
                km = j

    return km


def dive(i, d, n):
    j1 = i
    j2 = min_child(j1, d, n)
    while j2 != -1 and key[j1] > key[j2]:
        key[j1], key[j2] = key[j2], key[j1]
        name[j1], name[j2] = name[j2], name[j1]
        j1 = j2
        j2 = min_child(j1, d, n)


def emersion(i, d):
    j1 = i
    j2 = father(j1, d)
    while (j1 != 0) and key[j1] < key[j2]:
        key[j1], key[j2] = key[j2], key[j1]
        name[j1], name[j2] = name[j2], name[j1]
        j1 = j2
        j2 = father(j1, d)


def get_root(d, n):
    name_root = name[0]
    key_root = key[0]
    name[0] = name[n - 1]
    key[0] = key[n - 1]
    name.pop()
    key.pop()
    n -= 1
    if n > 1:
        dive(0, d, n)

    return name_root, key_root, n


def build_heap(d, n):
    for i in range(n - 1, -1, -1):
        dive(i, d, n)


def dijkstra_dheap(adj_matrix, n, d, start):
    up = []
    dist = []
    # Представим d-кучу массивом имен name[1..n] и массивом ключей key[1..n] так,
    # что key[i] является текущей оценкой длины кратчайшего пути от вершины s к вершине name[i].
    global name
    name = []
    global key
    key = []
    for i in range(0, n):
        up.append(0)
        dist.append(float("inf"))
        name.append(i)
        key.append(float("inf"))

    key[start] = 0
    build_heap(d, n)
    while n > 0:
        name_root, key_root, n = get_root(d, n)
        dist[name_root] = key_root
        for i_name, point in enumerate(adj_matrix[name_root]):
            if point != 0:
                try:
                    i_index = name.index(i_name)
                except:
                    i_index = None
                if i_index is not None:
                    if dist[i_name] == float("inf"):
                        if key[i_index] > dist[name_root] + point:
                            key[i_index] = dist[name_root] + point
                            emersion(i_index, d)
                            up[i_name] = name_root

    return dist, up