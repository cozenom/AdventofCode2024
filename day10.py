data = open("day10.txt").read().strip()

# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

data = [i for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1

# a hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1
# at each step. Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of
# the map).
h = len(data)
w = len(data[0])
trailheads = []
for y in range(h):
    for x in range(w):
        if data[y][x] == '0': trailheads.append((x,y))


def getneighbors(point):
    x,y = point
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    neighbors = []
    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < w and
            0 <= new_y < h):
            neighbors.append((new_x, new_y))
    return neighbors


def dfs(start, visited=None):
    if visited is None:
        visited = set()
    x, y = start
    visited.add(start)

    current = int(data[y][x])
    count = 1 if current == 9 else 0

    total_nines = count
    for nx, ny in getneighbors(start):
        n = int(data[ny][nx])
        if (nx, ny) not in visited and n - current == 1:
            total_nines += dfs((nx, ny), visited)

    return total_nines


res = 0
for trailhead in trailheads:
    res += dfs(trailhead)

print("Part one: ")
print(res)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2

def dfs2(start, current_path=None):

    if current_path is None:
        current_path = []

    x, y = start
    current_path.append(start)

    current = int(data[y][x])
    found_paths = []
    for nx, ny in getneighbors(start):
        n = int(data[ny][nx])
        if n - current == 1:
            new_path = current_path.copy()
            paths = dfs2((nx, ny), new_path)
            found_paths.extend(paths)
    if current == 9: # or found_paths:
        found_paths.append(current_path)

    return found_paths


res = 0
for trailhead in trailheads:
    res += len(dfs2(trailhead))

print("Part two: ")
print(res)
