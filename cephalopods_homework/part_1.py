import math
from pprint import pprint

# input = [['123', '328', '51', '64'],
#          ['45', '64', '387', '23'],
#          ['6', '98', '215', '314'],
#          ['*', '+', '*', '+']]


input = []
with open('input.txt','r') as f:
    for line in f:
        parts = line.strip().split()
        input.append(parts)


def calculate_expression(data):
    expressions = data[-1]
    totals = []
    for i in range(len(data[0])):
        col_values = [ int(row[i]) for row in data[:-1] ]
        expression = expressions[i]
        if expression == '+':
            totals.append(sum(col_values))
        if expression == '*':
            totals.append(math.prod(col_values))
    print(totals)
    return sum(totals)



print(calculate_expression(input))
