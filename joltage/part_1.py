# input=['987654321111111',
#        '811111111111119',
#        '234234234234278',
#        '818181911112111']
input = []
with open('input.txt','r') as f:
    for line in f:
        input.append(line.strip())

def find_joltage(input):
    joltage = 0
    for val in input:
        digits = [int(x) for x in val]
        max_joltage = 0
        for i in range(len(digits)-1):
            for j in range(i+1, len(digits)):
                combined_joltage = int(f"{digits[i]}{digits[j]}")
                if combined_joltage > max_joltage:
                    max_joltage = combined_joltage
                    print(max_joltage)

        joltage += max_joltage
    return joltage

print(find_joltage(input))
