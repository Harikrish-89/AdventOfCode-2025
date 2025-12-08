from pprint import pprint

# puzzle_input = [
#     ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
#     ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
#     ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
#     ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
#     ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
#     ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
#     ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
#     ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
#     ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
#     ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.']
# ]

with open('input.txt','r') as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append(list(line.strip()))

pprint(puzzle_input)

print("###############################################################")

def find_accessible_roll_paper(roll_paper_map):
    removed_rolls = 0
    clone = [row[:] for row in roll_paper_map]
    for row in range(len(roll_paper_map)):
        for col in range(len(roll_paper_map[0])):
            if roll_paper_map[row][col] == '@' and is_accessible(roll_paper_map, row, col):
                clone[row][col] = '.'
                removed_rolls += 1
    pprint(clone)
    return removed_rolls, clone


def is_accessible(roll_paper_map, row, col):
    directions = [
        (0, 1),   # east
        (0, -1),  # west
        (1, 0),   # south
        (-1, 0),  # north
        (-1, 1),  # northwest
        (-1, -1), # northeast
        (1, 1),   # southwest
        (1, -1)   # southeast
    ]

    rows = len(roll_paper_map)
    cols = len(roll_paper_map[0])

    adjacent_rolls = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if roll_paper_map[nr][nc] == '@':
                adjacent_rolls += 1

    return adjacent_rolls < 4

def remove_all_rolls(current_map):
    total_removed = 0
    while True:
        removed, new_map = find_accessible_roll_paper(current_map)
        if removed == 0:
            break
        total_removed += removed
        current_map = new_map
    return total_removed

print(remove_all_rolls(puzzle_input))

