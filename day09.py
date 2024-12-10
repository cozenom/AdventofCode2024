from collections import defaultdict
from tqdm import tqdm

data = open("day09.txt").read().strip()
# data = """2333133121414131402"""

# ----------------------------------------------------------------------------------------------------------------------
# Part 1

start_diskmap = dict()
spaces = []
pos = 0
filenr = 0
for i, n in enumerate(data):
    if i % 2:
        for j in range(int(n)):
            start_diskmap[pos] = 'space'
            spaces.append(pos)
            pos += 1
    else:
        for j in range(int(n)):
            start_diskmap[pos] = filenr
            pos += 1
        filenr += 1

diskmap = start_diskmap.copy()
end = False
for space in spaces:
    for i in reversed(diskmap.keys()):
        if i < space:
            end = True
            break
        if diskmap[i] != 'space':
            # swap
            diskmap[space] = diskmap[i]
            diskmap[i] = 'space'
            break
    if end:
        break

checksum = 0
for i in diskmap.keys():
    if diskmap[i] == 'space': break
    v = int(diskmap[i])
    checksum += i * v

# print(''.join(str(x) if x != 'space' else '.' for x in start_diskmap.values()))
print("Part one: ")
print(checksum)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

# This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt
# to move each file exactly once in order of decreasing file ID number starting with the file with the highest file
# ID number. If there is no span of free space to the left of a file that is large enough to fit the file,
# the file does not move.

inverse_diskmap = defaultdict(list)
for k, v in start_diskmap.items():
    inverse_diskmap[v].append(k)

spacegroups = []
currentgroup = []
for space in spaces:
    if len(currentgroup) > 0:
        last = currentgroup[-1]
        if (space - last) == 1:
            currentgroup.append(space)
        else:
            spacegroups.append(currentgroup)
            currentgroup = [space]
    else:
        currentgroup.append(space)

diskmap = start_diskmap.copy()
end = False
for file_id in tqdm(reversed(inverse_diskmap.keys()), bar_format='{bar:10}'):
    if file_id != 'space':
        for j, spacegroup in enumerate(spacegroups):
            if len(spacegroup) == 0: continue
            sg_size = len(spacegroup)
            file_size = len(inverse_diskmap[file_id])
            file_pos = inverse_diskmap[file_id][0]
            sg_pos = spacegroup[0]
            # print(file_id, inverse_diskmap[file_id], file_size, spacegroup, sg_size, sg_size >= file_size, sg_size-file_size)
            if sg_size >= file_size and file_pos > sg_pos:
                # can put - has space
                newspace = []
                newspacegroup = []
                for i, space in enumerate(spacegroup):
                    if i < file_size:
                        newspace.append(space)
                    else:
                        newspacegroup.append(space)
                inverse_diskmap[file_id] = newspace
                spacegroups[j] = newspacegroup
                break

s = ['.'] * len(diskmap)
for i in inverse_diskmap.keys():
    if i != 'space':
        for j in inverse_diskmap[i]:
            s[j] = i

checksum = 0
for i, v in enumerate(s):
    if v != '.':
        checksum += i * v

# print(''.join(str(x) for x in s))
print("Part two: ")
print(checksum)
