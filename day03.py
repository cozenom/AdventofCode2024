import re

data = open("day03.txt").read().strip()
print(data)
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Scan the corrupted memory for uncorrupted mul instructions.
# What do you get if you add up all of the results of the multiplications?

res = 0
strings = re.findall("mul\(\d+,\d+\)", data)
for i in strings:
    nums = [int(j) for j in i[4:-1].split(',')]
    res += nums[0] * nums[1]

print("Part one: ")
print(res)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
# There are two new instructions you'll need to handle:
#     The do() instruction enables future mul instructions.
#     The don't() instruction disables future mul instructions.

res = 0
strings = re.findall("(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don't\(\))", data)
on = True
for i in strings:
    if i == "don't()":
        on = False
    elif i == "do()":
        on = True
    elif on and i[0:3] == "mul":
        nums = [int(j) for j in i[4:-1].split(',')]
        res += nums[0] * nums[1]

print("Part two: ")
print(res)