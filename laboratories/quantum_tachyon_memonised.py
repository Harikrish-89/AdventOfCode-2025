from copy import deepcopy
from pprint import pprint

puzzle_input = []
with open("input.txt", "r") as f:
    for line in f:
        puzzle_input.append([s for s in line.strip()])


def start_beam(start, tachyon_map):
    stack = [(start, 0)]
    memo = {}
    while stack:
        (r, c), phase = stack.pop()
        if (r, c) in memo:
            continue
        if phase == 0:
            if r == len(tachyon_map) - 1:
                memo[(r, c)] = 1
                continue
            stack.append(((r, c), 1))
            if tachyon_map[r][c] == '^':
                stack.append(((r, c - 1), 0))
                stack.append(((r, c + 1), 0))
            elif tachyon_map[r][c] == '.':
                stack.append(((r + 1, c), 0))
        else:
            memo[(r, c)] = memo[(r, c - 1)] + memo[(r, c + 1)] if tachyon_map[r][c] == '^' else memo.get((r + 1, c), 0)
    return memo[start]


def find_no_of_splits(tachyon_map):
    start_i, start_j = 0, tachyon_map[0].index('S')
    return start_beam((start_i + 1, start_j), tachyon_map)


print(find_no_of_splits(puzzle_input))
