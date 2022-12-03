filepath = 'data/day3.txt'

def find_common(strng):
    common = set.intersection(*map(set,strng))
    for c in common:
        return c

def find_error(sack):
    half = int(len(sack)/2)
    compartments = [sack[:half], sack[half:]]
    return find_common(compartments)

def find_badge(sack1, sack2, sack3):
    sacks = [sack1, sack2, sack3]
    return find_common(sacks)

def get_priority(item):
    if item < 'a':
        # uppercase item
        return ord(item) - 65 + 27
    else:
        # lowercase item
        return ord(item) - 96

with open(filepath) as f:
    sacks = f.read().split('\n')

part1_prio = 0
part2_prio = 0

for sack in sacks:
    part1_prio += get_priority(find_error(sack))

print(part1_prio)

i = 0
while i < len(sacks):
    part2_prio += get_priority(find_badge(sacks[i], sacks[i+1], sacks[i+2]))
    i+=3

print(part2_prio)
    