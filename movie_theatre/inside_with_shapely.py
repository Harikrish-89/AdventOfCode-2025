from itertools import combinations

import numpy as np
import shapely

with open('input.txt', 'r') as f:
    theatre_map = []
    for line in f:
        theatre_map.append([int(x) for x in line.strip().split(',')])

polygon = shapely.Polygon(theatre_map)
largest_area = 0
for p1, p2 in combinations(theatre_map, 2):
    x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
    y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
    if polygon.contains(shapely.box(x_min, y_min, x_max, y_max)):
        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        largest_area_p2 = max(largest_area, area)

print(largest_area)
