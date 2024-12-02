data = open("day01.txt").read().strip()
data = [[int(j) for j in i.split("   ")] for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
first = sorted([i[0] for i in data])
second = sorted([i[1] for i in data])

dist = 0

for i in range(len(first)):
    f, s = first[i], second[i]
    dist += abs(f-s)

print("Part one: ")
print(dist)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

similarity_score = 0

for i in first:
    similarity_score += second.count(i) * i

print("Part two: ")
print(similarity_score)
