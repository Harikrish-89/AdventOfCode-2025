from copy import deepcopy
from pprint import pprint

puzzle_input = []
with open("sample_input.txt", "r") as f:
    for line in f:
        puzzle_input.append([s for s in line.strip()])


def start_beam(start, tachyon_map):
    path = [start]
    stack = [(start, deepcopy(path), deepcopy(tachyon_map))]
    count = 0
    while stack:
        (r, c), path, curr_map = stack.pop()
        if r == len(tachyon_map) - 1:
            count += 1
            print("I'm reaching end", count)
            continue
        if curr_map[r][c] == '^':
            if c - 1 >= 0 and curr_map[r][c - 1] == '.':
                new_map = deepcopy(curr_map)
                new_map[r][c - 1] = '|'
                new_path = deepcopy(path)
                new_path.append((r, c - 1))
                stack.append(((r, c - 1), new_path, new_map))
            if c + 1 < len(tachyon_map[0]) and curr_map[r][c + 1] == '.':
                new_map = deepcopy(curr_map)
                new_map[r][c + 1] = '|'
                new_path = deepcopy(path)
                new_path.append((r, c + 1))
                stack.append(((r, c + 1), new_path, new_map))
        elif curr_map[r][c] == '.' and r -1 >=0 and (curr_map[r - 1][c] == '|' or curr_map[r - 1][c] == 'S'):
            curr_map[r][c] = '|'
            new_map = deepcopy(curr_map)
            new_path = deepcopy(path)
            new_path.append((r+1, c))
            stack.append(((r+1, c), new_path, new_map))
        elif curr_map[r][c] == '|':
            new_map = deepcopy(curr_map)
            new_path = deepcopy(path)
            new_path.append((r+1, c))
            stack.append(((r+1, c), new_path, new_map))
    return count


def find_no_of_splits(tachyon_map):
    start_i, start_j = 0, tachyon_map[0].index('S')
    return start_beam((start_i + 1, start_j), tachyon_map)


print(find_no_of_splits(puzzle_input))
