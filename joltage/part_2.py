# input=['987654321111111',
#        '811111111111119',
#        '234234234234278',
#        '818181911112111']
input = []
with open('input.txt','r') as f:
    for line in f:
        input.append(line.strip())


def find_joltage(input):
    max_joltages = []
    for val in input:
        maximas=[]
        digits = [int(x) for x in val]
        start = 0
        for i in range(11,-1,-1):
            local_maxima = max(digits[start:len(digits)-i])
            local_maxima_index = digits.index(local_maxima, start)
            maximas.append(local_maxima)
            start = local_maxima_index +1
        max_joltages.append(int("".join(str(x) for x in maximas)))
    return sum(max_joltages)


print(find_joltage(input))
