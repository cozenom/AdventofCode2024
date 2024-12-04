data = open("day02.txt").read().strip()

data = [[int(j) for j in i.split(" ")] for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# So, a report only counts as safe if both of the following are true:
#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

safe_reports = 0
for row in data:
    pos = 0
    last = -1
    issafe = True

    for curr in row:
        if last != -1:
            diff = last - curr
            if pos == 0:
                if diff > 0:
                    pos = 1
                else:
                    pos = -1

            if abs(diff) > 3 or (diff <= 0 and pos == 1) or (diff >= 0 and pos == -1):
                issafe = False
                break
        last = curr

    if issafe:
        safe_reports += 1

print("Part one: ")
print(safe_reports)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level
# in what would otherwise be a safe report. It's like the bad level never happened!


def checkrow(row):
    if len(row) <= 1:
        return True
    increasing = row[0] < row[-1]

    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False
    return True


safe_reports = 0
for row in data:
    if not checkrow(row):
        for i in range(len(row)):
            newrow = [y for x,y in enumerate(row) if x != i]
            if checkrow(newrow):
                # Safe combo found
                # print(newrow)
                safe_reports += 1
                break
    else:
        # Safe - no changes
        safe_reports += 1


print("Part two: ")
print(safe_reports)
