from collections import deque

data = open("day12.txt").read()

# data = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """

data = data.strip().split('\n')

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
h = len(data)
w = len(data[0])

# Find prod of groups and perimiter of groups


visited = set()
groups = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# Find groups
def bfs(startpos):
    startx, starty = startpos
    startletter = data[starty][startx]
    current_group = set()
    queue = deque([startpos])

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        current_group.add((x, y))

        for dx, dy in dirs:
            newx, newy = x + dx, y + dy
            if 0 <= newx < w and 0 <= newy < h and data[newy][newx] == startletter and (newx, newy) not in visited:
                queue.append((newx, newy))
    return current_group


for y in range(h):
    for x in range(w):
        if (x, y) not in visited:
            groups.append(bfs((x, y)))


# Find prod of area and perimeter of groups

def getperim(group):
    perimeter = 0
    for x, y in group:
        for dx, dy in dirs:
            newx, newy = x + dx, y + dy
            if not (0 <= newx < h and 0 <= newy < w) or (newx, newy) not in group:
                perimeter += 1
    return perimeter


res = 0
for group in groups:
    res += len(group) * getperim(group)

print("Part one: ")
print(res)


# ----------------------------------------------------------------------------------------------------------------------
# Part 2

# Find prod of area and number of sides

def check_same(pos, plant):
    x, y = pos
    if 0 <= x < w and 0 <= y < h:
        if data[y][x] == plant: return True
    return False


def check_corners(pos):
    x, y = pos
    plant = data[y][x]
    NW, W, SW, N, S, NE, E, SE = check_same((x - 1, y - 1), plant), check_same((x - 1, y), plant), check_same(
        (x - 1, y + 1), plant), check_same((x, y - 1), plant), check_same((x, y + 1), plant), check_same((x + 1, y - 1),
                                                                                                         plant), check_same(
        (x + 1, y), plant), check_same((x + 1, y + 1), plant)

    edges = sum([
        N and E and not NE,
        N and W and not NW,
        S and E and not SE,
        S and W and not SW,
        not (N or W),
        not (W or S),
        not (S or E),
        not (E or N)
    ])
    return edges


res = 0
for group in groups:
    seen = set()
    corners = 0
    plant = None
    for pos in group:
        corners += check_corners(pos)
    res += len(group) * corners

print("Part two: ")
print(res)