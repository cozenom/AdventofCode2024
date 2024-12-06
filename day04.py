data = open("day04.txt").read().strip()

# data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

data = data.split("\n")

[print(i) for i in data]
print('\n')
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Find XMAS
w = len(data[0])
h = len(data)
count = 0

def check_word(x, y, dx, dy):
    if not (0 <= x + 3 * dx < w and 0 <= y + 3 * dy < h):
        return False
    word = ''
    for i in range(4):  # XMAS
        word += data[y + i * dy][x + i * dx]
    return word == 'XMAS'


for y in range(w):
    for x in range(h):
        if data[y][x] == "X":
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if check_word(x, y, dx, dy):
                    count += 1

print("Part one: ")
print(count)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
# M.S
# .A.
# M.S
def check_word2(x, y):
    if x == 0 or y == 0 or x == w-1 or y == h-1:
        return False
    r=0
    for dx, dy in [(-1, -1), (-1, 1)]:
        if data[y+dy][x+dx]=="M" and data[y-dy][x-dx]=="S" or data[y+dy][x+dx]=="S" and data[y-dy][x-dx]=="M":r+=1

    if r ==2:
        return True
    else: return False

count2 = 0
for y in range(w):
    for x in range(h):
        if data[y][x] == "A":
            if check_word2(x,y):
                count2 +=1


print("Part two: ")
print(count2)
