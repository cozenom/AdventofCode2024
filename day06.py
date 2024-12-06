data = open("day06.txt").read().strip()
# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

data = [i for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
w = len(data[0])
h = len(data[1])

blocked = set()
pos = None

for y in range(h):
    for x in range(w):
        if data[y][x] == '#':
            blocked.add((x,y))
        elif data[y][x] == '^':
            pos = (x,y)

steps = 0
turns = 0
visited = [pos]
dirs = [(0,-1), (1,0), (0,1), (-1,0)] #NESW

while pos[0] in range(w) and pos[1] in range(h):
    dir = dirs[turns%4]
    next = (pos[0]+dir[0], pos[1]+dir[1])
    if next not in blocked:
        pos = next
        steps += 1
    else:
        turns += 1
    visited.append(pos)

print("Part one: ")
print(len(set(visited)) -1 ) # -1 for the one going out of bounds
# ----------------------------------------------------------------------------------------------------------------------
# Part 2


print("Part two: ")
print()