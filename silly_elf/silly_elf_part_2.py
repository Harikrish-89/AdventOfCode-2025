import re


# puzzle_input= ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224',
#                '1698522-1698528','446443-446449','38593856-38593862','565653-565659',
#                '824824821-824824827','2121212118-2121212124']

puzzle_input = ['197-407', '262128-339499', '557930-573266', '25-57', '92856246-93001520', '2-12',
                '1919108745-1919268183', '48414903-48538379', '38342224-38444598', '483824-534754', '1056-1771',
                '4603696-4688732', '75712519-75792205', '20124-44038', '714164-782292', '4429019-4570680',
                '9648251-9913729', '6812551522-6812585188', '58-134', '881574-897488', '648613-673853',
                '5261723647-5261785283', '60035-128980', '9944818-10047126', '857821365-857927915', '206885-246173',
                '1922-9652', '424942-446151', '408-1000']
non_id_pattern= '^0'


def check_naughty(val):
    pattern =  r'^(.*?)\1+$'
    matched = re.match(pattern, val)
    if not matched:
       return 0
    seq = matched.group(1)
    if len(val)% len(seq) == 0:
        return val
    else:
        return 0

total=0

for id_range in puzzle_input:
    start_range, end_range = id_range.split('-')
    start = int(start_range)
    end = int(end_range)
    match = re.match(non_id_pattern, start_range)
    if match:
        continue
    for elf_id in range(start, end + 1):
            elf_id_str = str(elf_id)
            naughty = int(check_naughty(elf_id_str))
            total += naughty

print(total)


