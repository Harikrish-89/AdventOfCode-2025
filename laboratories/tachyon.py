from pprint import pprint

puzzle_input = []
with open("sample_input.txt", "r") as f:
    for line in f:
        puzzle_input.append([s for s in line.strip()])

def start_beam(visited, start, tachyon_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    splits = 0
    stack = [start]
    while stack:
        r, c = stack.pop()
        if 0 <= r < len(tachyon_map) and 0 <= c < len(tachyon_map[0]) and (r, c) not in visited:
            visited.add((r, c))
            if tachyon_map[r][c] == 'S':
                tachyon_map[r + 1][c] = '|'
            elif tachyon_map[r][c] == '^' and r - 1 >= 0 and tachyon_map[r - 1][c] == '|':
                splits += 1
                tachyon_map[r][c + 1] = '|'
                tachyon_map[r][c - 1] = '|'
            elif tachyon_map[r][c] == '|' and r + 1 < len(tachyon_map) and tachyon_map[r + 1][c] == '.':
                tachyon_map[r + 1][c] = '|'
            elif tachyon_map[r][c] == '.' and r - 1 >= 0 and tachyon_map[r - 1][c] == '|':
                tachyon_map[r][c] = '|'
            for dr, dc in directions:
                stack.append((r + dr, c + dc))
    pprint(tachyon_map)
    return splits


def find_no_of_splits(tachyon_map):
    start_i, start_j = 0, tachyon_map[0].index('S')
    visited = set()
    return start_beam(visited, (start_i, start_j), tachyon_map)


print(find_no_of_splits(puzzle_input))
