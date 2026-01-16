from pprint import pprint

import matplotlib.pyplot as plt

with open('sample_input.txt','r') as f:
    theatre_map = []
    for line in f:
        theatre_map.append([int(x) for x in line.strip().split(',')])
borders_ref = []
borders_c= {}
borders_r = {}
green_tiles = []

def scan_line_intersection():
    for point in borders_ref:
        c = point[0]
        r = point[1]
        if c not in borders_c:
            borders_c[c] = set()
        borders_c[c].add(r)

def within_borders(point):
    c = point[0]
    r = point[1]
    c_intersections = list(set(sorted(borders_c.get(c, []))))
    slices = [[c_intersections[0]]]
    for i in range(1, len(c_intersections)):
        if c_intersections[i] - c_intersections[i-1] > 1:
            slices.append([c_intersections[i]])
        else:
            slices[-1].append(c_intersections[i])
    print("slices for point", point, ":", slices)
    for sl in slices:
        min_sl = min(sl)
        max_sl = max(sl)
        if not (min_sl < r < max_sl):
            return False
    return True



def find_largest_inside():
    find_borders()
    scan_line_intersection()
    plot_polygon()
    print(borders_ref)
    print(borders_c)
    max_area = 0
    min_row, min_col, max_row, max_col = 0, 0, 0, 0
    area_c = {}
    for i in range(len(theatre_map)):
        for j in range(len(theatre_map)):
            if i == j:
                continue
            first_r = theatre_map[i][1]
            first_c = theatre_map[i][0]
            second_r = theatre_map[j][1]
            second_c = theatre_map[j][0]
            if first_r == second_r or first_c == second_c:
                continue
            if not within_borders([first_c, second_r]) or not within_borders([second_c, first_r]):
                print("Not within borders:", first_c, second_r, second_c, first_r)
                continue
            max_row = max(first_r, second_r) + 1
            min_row = min(first_r, second_r)
            max_col = max(first_c, second_c) + 1
            min_col = min(first_c, second_c)
            max_area = max(max_area, (max_row - min_row) * (max_col - min_col))
            area = (max_row - min_row) * (max_col - min_col)
            print("area found:", area, min_row, min_col, max_row, max_col)
            max_area = max(max_area, area)
            area_c[area] = (min_row, min_col, max_row, max_col)
    print(max_area)
    min_row, min_col, max_row, max_col = area_c[max_area]
    visualize(min_row, min_col, max_row-1, max_col-1)
    return max_area


def visualize_theatre_map():
    xs = [x[0] for x in theatre_map]
    ys = [y[1] for y in theatre_map]
    plt.figure(figsize=(20, 18))
    plt.scatter(xs, ys, c="red", s=10, label=f"{xs},{ys}")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True)
    for x, y in theatre_map:
        plt.annotate(
            f"({x},{y})",
            (x, y),
            textcoords="offset points",
            xytext=(5, 5),
            fontsize=8
        )
    plt.show()


def visualize(min_col, min_row, max_col, max_row):
    plot_polygon()
    print("visualizing...", min_row, min_col, max_row, max_col)
    x1, y1 = min_row, min_col
    x2, y2 = max_row, max_col

    plt.gca().add_patch(
        plt.Rectangle(
            (x1, y1),
            x2 - x1,
            y2 - y1,
            fill=False,
            edgecolor="blue",
            linewidth=2,
            label="Rectangle"
        )
    )
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_polygon():
    xs = [x[0] for x in borders_ref]
    ys = [y[1] for y in borders_ref]
    plt.figure(figsize=(8, 6))
    plt.scatter(xs, ys, c="red", s=10)
    xs_loop = xs + [xs[0]]
    ys_loop = ys + [ys[0]]
    gx = [x[0] for x in green_tiles]
    gy = [y[1] for y in green_tiles]
    plt.scatter(gx, gy, c="green", s=10)
    plt.plot(xs_loop, ys_loop, color="green", linewidth=1)
    plt.show()


def find_borders():
    for i in range(len(theatre_map)):
        borders_ref.append(theatre_map[i])
        for j in range(i + 1, len(theatre_map)):
            first_r = theatre_map[i][1]
            first_c = theatre_map[i][0]
            second_r = theatre_map[j][1]
            second_c = theatre_map[j][0]
            min_c = min(first_c, second_c)
            max_c = max(first_c, second_c)
            min_r = min(first_r, second_r)
            max_r = max(first_r, second_r)
            if min_c == max_c:
                for r in range(min_r, max_r):
                    borders_ref.append([min_c, r])
            if min_r == max_r:
                for c in range(min_c, max_c):
                    borders_ref.append([c, min_r])

print(find_largest_inside())
