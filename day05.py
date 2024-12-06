data = open("day05.txt").read().strip()

data = data.split('\n\n')
rules = [[int(j) for j in i.split('|')] for i in data[0].split('\n')]
seqs = [[int(j) for j in i.split(',')] for i in data[1].split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
res = 0
incorrect = []

for seq in seqs:
    valid = True
    for rule in rules:
        if(rule[0] in seq and rule[1] in seq):
            if seq.index(rule[0]) > seq.index(rule[1]):
                incorrect.append(seq)
                valid = False
                break
    if valid:
        res += seq[len(seq)//2]



print("Part one: ")
print(res)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

res = 0
for seq in incorrect:
    reldict = {i:[] for i in seq}
    indegrees = {i:0 for i in seq}
    relevant = []
    for rule in rules:
        if rule[0] in seq and rule[1] in seq:
            relevant.append(rule)
            reldict[rule[0]].append(rule[1])
            indegrees[rule[1]] += 1

    queue = [i for i in indegrees.keys() if indegrees[i] == 0]
    new = []
    while queue:
        curr = queue.pop(0)
        new.append(curr)

        for neighbor in reldict[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    res += new[len(new)//2]

print("Part two: ")
print(res)
