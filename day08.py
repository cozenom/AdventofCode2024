from collections import defaultdict

data = open("day08.txt").read().strip()

# data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

data = [i for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
w = len(data[0])
h = len(data)

posdict = defaultdict(list)

for y, line in enumerate(data):
    for x, val in enumerate(line):
        if data[y][x] != '.':
            posdict[data[y][x]].append((x, y))


def getdist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def getanti(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    diffx, diffy = x2 - x1, y2 - y1

    op1 = (x1 - diffx, y1 - diffy)
    op2 = (x2 + diffx, y2 + diffy)
    antinodes = []
    if (getdist(a, op1) * 2 == getdist(b, op1)) and op1[0] in range(w) and op1[1] in range(h):
        antinodes.append(op1)
    if (getdist(a, op2) == 2 * getdist(b, op2)) and op2[0] in range(w) and op2[1] in range(h):
        antinodes.append(op2)
    return antinodes


antinodes = set()
antinodedict = defaultdict(list)
for k, v in posdict.items():
    for i in v:
        for j in v:
            if i == j:
                continue
            anti = getanti(i, j)
            antinodedict[k].append(anti)
            for a in anti:
                antinodes.add(a)

print("Part one: ")
print(len(antinodes))


# ----------------------------------------------------------------------------------------------------------------------
# Part 2


def getanti2(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    diffx, diffy = x2 - x1, y2 - y1
    print(a, b, getdist(i, j), diffx, diffy)
    antinodes = [a,b ]
    op1 = (x1 - diffx, y1 - diffy)
    while op1[0] in range(w) and op1[1] in range(h):
        print(op1, 'op1')
        antinodes.append(op1)
        op1 = (op1[0] - diffx, op1[1] - diffy)

    op2 = (x2 + diffx, y2 + diffy)
    while op2[0] in range(w) and op2[1] in range(h):
        print(op2, 'op2')
        antinodes.append(op2)
        op2 = (op2[0] + diffx, op2[1] + diffy)

    return antinodes


antinodes = set()
antinodedict = defaultdict(list)

for k, v in posdict.items():
    print(k, v)
    for i in v:
        for j in v:
            if i == j:
                continue
                ##
            anti = getanti2(i, j)
            antinodedict[k].append(anti)

            for a in anti:
                antinodes.add(a)
            print(antinodes)


print(antinodes)
print(antinodedict)
print("Part two: ")
print(len(antinodes))
