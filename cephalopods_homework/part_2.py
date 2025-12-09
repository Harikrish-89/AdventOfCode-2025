import math
from pprint import pprint


with open('input.txt','r', encoding="utf-8") as f:
    input_puzzle = [line.rstrip("\n") for line in f]
### We need to pad for the max len or else transpose will not work
max_len = max(len(line) for line in input_puzzle)
padded = [line.ljust(max_len) for line in input_puzzle]
def calculate_expression():
    # Simple transpose in python
    columns = list(zip(*padded))
    separated_columns = []
    tmp_array = []
    for col in columns:
        if all(x == ' ' for x in col):
            separated_columns.append(tmp_array)
            tmp_array=[]
            continue
        tmp_array.append(col)
    separated_columns.append(tmp_array)
    problem_answers=[]
    for math_problems in separated_columns:
        expression = math_problems[0][-1]
        if expression == '+':
            tmp=0
        else:
            tmp=1
        for i in range(len(math_problems)):
            if expression == '*':
                tmp = tmp * int("".join(math_problems[i]).replace(expression,''))
            if expression == '+':
                tmp = tmp + int("".join(math_problems[i]).replace(expression,''))
        problem_answers.append(tmp)
    return sum(problem_answers)



print(calculate_expression())
