from collections import defaultdict

data = open("day11.txt").read().strip()

# data = """125 17"""


data = [int(i) for i in data.split(' ')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1

# Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:
#
# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

def blink(input):
    new = []

    for stone in input:
        if stone == 0:
            new.append(1)
        elif len(str(stone))%2 == 0:
            mid = len(str(stone))//2
            new.append(int(str(stone)[:mid]))
            new.append(int(str(stone)[mid:]))
        else:
            new.append(stone * 2024)
    return new

stones = data.copy()
for i in range(25):
    stones = blink(stones)

print("Part one: ")
print(len(stones))
# ----------------------------------------------------------------------------------------------------------------------
# Part 2


stones = data.copy()
stonesdict = {i:1 for i in stones} # lazy

def blink2(stones):
    next = defaultdict(int)

    for stone, count in stones.items():
        if stone == 0:
            next[1] += count
        elif len(str(stone)) % 2 == 1:
            next[stone*2024] += count
        else:
            # even
            mid = len(str(stone))//2
            next[int(str(stone)[:mid])] += count
            next[int(str(stone)[mid:])] += count
    return next

for i in range(75):
    stonesdict = blink2(stonesdict)

print("Part two: ")
print(sum([i for i in stonesdict.values()]))
