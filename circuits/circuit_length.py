import math
from collections import Counter
from pprint import pprint

from circuits.union_find import UnionFind

puzzle_input = []




with open('input.txt', 'r+') as file:
    for line in file:
        puzzle_input.append(line.strip().split(','))


def euclidean_distance(start, end):
    sx, sy, sz = start
    ex, ey, ez = end
    return ((ex - sx) ** 2 + (ey - sy) ** 2 + (ez - sz) ** 2) ** 0.5



def find_all_closest(circuit_map):
    all_closest = {}
    union_find = UnionFind()
    for point in circuit_map:
        point = tuple(map(int, point))
        union_find.add(point)
    for i in range(len(circuit_map)):
        point_a = tuple(map(int, circuit_map[i]))
        for j in range(len(circuit_map)):
            if i == j:
                continue
            point_b = tuple(map(int, circuit_map[j]))
            distance = euclidean_distance(point_a, point_b)
            all_closest[distance] = point_a,point_b
    sorted_dist = dict(sorted(all_closest.items(), key=lambda item: item[0])[:1000])
    for dist in sorted_dist:
        point_a, point_b = sorted_dist[dist]
        if union_find.find(point_a) != union_find.find(point_b):
            union_find.union(point_a, point_b)
    print(Counter(union_find.find(p) for p in union_find.parent))
    print(list(set(Counter(union_find.find(p) for p in union_find.parent).values())))
    return math.prod(list(set(Counter(union_find.find(p) for p in union_find.parent).values()))[-3:])

print(find_all_closest(puzzle_input))
