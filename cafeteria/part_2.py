# ranges=["3-5",
#         "10-14",
#        "16-20",
#         "9-22",
#         "10-14",
#         "12-18"]
# input_list = [1, 5, 8, 11, 17, 32]

ranges=[]
input_list=[]

with open('input.txt','r') as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        if "-"  in line:
            ranges.append(line.strip())
        else:
            input_list.append(line.strip())

print(ranges)
print(input_list)



def find_fresh(database, items):
    print("Finding fresh items")
    fresh_id_ranges = []
    for r in database:
        start, end = map(int, r.split('-'))
        fresh_id_ranges.append([int(start), int(end)])
    print("Fresh ID Ranges:", fresh_id_ranges)
    fresh_id_ranges.sort()
    print("Sorted ranges:", fresh_id_ranges)
    merged = [fresh_id_ranges[0]]
    for current in fresh_id_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    print("Merged ranges:", merged)
    total=0
    for r in merged:
        total += (r[1]-r[0])+1
    return total



print(find_fresh(ranges, input_list))

