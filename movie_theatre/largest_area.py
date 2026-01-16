with open('input.txt', 'r') as f:
    theatre_map = []
    for line in f:
        theatre_map.append([int(x) for x in line.strip().split(',')])

def find_largest_area():
    largest_area = 0
    for i in theatre_map:
        for j in theatre_map:
            if i==j:
                continue
            max_row = max(i[0], j[0])+1
            min_row = min(i[0], j[0])
            max_col = max(i[1], j[1])+1
            min_col = min(i[1], j[1])
            area = (max_row  - min_row) * (max_col  - min_col)
            largest_area = max(largest_area, area)
    return largest_area

print(find_largest_area())
