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
h = len(data)

blocked = set()

for y in range(h):
    for x in range(w):
        if data[y][x] == '#':
            blocked.add((x, y))
        elif data[y][x] == '^':
            startpos = (x, y)

steps = 0
turns = 0
visited = [startpos]
pos = startpos

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  #NESW

while pos[0] in range(w) and pos[1] in range(h):
    dir = dirs[turns % 4]
    next = (pos[0] + dir[0], pos[1] + dir[1])
    if next not in blocked:
        pos = next
        steps += 1
    else:
        turns += 1
    visited.append(pos)

print("Part one: ")
print(len(set(visited)) - 1)  # -1 for the one going out of bounds

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

# If you revisit a tile with a turning of 1 away
print(f"Startpos {startpos}")
print(f"W: {w}, H: {h}")

turns = 0
visited = [(startpos, turns)]
pos = startpos

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  #NESW

def checkloop(block):
    newblocked = blocked | {block}
    seen = set()
    facing = 0
    pos = startpos
    # walk
    while pos[0] in range(w) and pos[1] in range(h):
        current = (pos, facing)
        if current in seen:
            return True
        seen.add(current)

        dir = dirs[facing]
        nextpos = (pos[0] + dir[0], pos[1] + dir[1])
        nextfacing = (facing + 1) % 4

        if nextpos not in newblocked:
            pos = nextpos
        else:
            facing = nextfacing
    return False


resblocks = set()
# See if placing the block on the next step of the path would create a loop
while pos[0] in range(w) and pos[1] in range(h):
    dir = dirs[turns]
    next = (pos[0] + dir[0], pos[1] + dir[1])
    nextturn = (turns + 1) % 4

    if checkloop(next):
        resblocks.add(next)
    if next not in blocked:
        pos = next
    else:
        turns = (turns + 1) % 4

print(visited)
print("Part two: ")
print(len(resblocks))
