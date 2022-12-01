elves = []

# add first elf
i = 0
elves.append(0)

with open('data/day1.txt') as f:
    lines = f.read().split('\n')

for l in lines:
    try:
        elves[i] += float(l)
    except ValueError as e:
        # new line - so move on to next elf
        elves.append(0)
        i += 1

# part 1
print max(elves)

elves.sort(reverse=True)

# part 2
print(elves[0] + elves[1] + elves[2])