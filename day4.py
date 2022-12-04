filepath = "data/day4.txt"

def toset(assignemnt):
    splt = assignemnt.split('-')

    out = set()

    start = int(splt[0])
    end = int(splt[1])

    out.add(start)

    i = start
    while i <= end:
        out.add(i)
        i+=1

    return out

def get_common_assignments(ass1, ass2):
    return ass1.issubset(ass2) or ass2.issubset(ass1)
    
def get_overlap_assignments(ass1, ass2):
    return bool(ass1 & ass2)

def get_solutions(assignemnts):
    splt = assignemnts.split(',')
    
    elfass1 = toset(splt[0])
    elfass2 = toset(splt[1])

    return get_common_assignments(elfass1, elfass2), get_overlap_assignments(elfass1, elfass2)

with open(filepath) as f:
    lines = f.read().split('\n')

soln1 = 0
soln2 = 0

for line in lines:
    one, two = get_solutions(line)
    soln1 += one
    soln2 += two

print(soln1, soln2)