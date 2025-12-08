# ranges=["3-5",
#         "10-14",
#        "16-20",
#         "12-18"]
# input_list = [1, 5, 8, 11, 17, 32]
ranges=[]
input_list=[]

with open('input.txt','r') as f:
    for line in f:
        if "-"  in line:
            ranges.append(line.strip())
        else:
            input_list.append(line.strip())

print(ranges)
print(input_list)

def find_fresh(database, items):
    print("Finding fresh items")
    fresh_items = set()
    for r in database:
        start, end = map(int, r.split('-'))
        for item in items:
            item_value = int(item)
            if start <= item_value <= end:
                fresh_items.add(item)
    print("Fresh items:", fresh_items)
    return len(fresh_items)

print(find_fresh(ranges, input_list))
