from tqdm import tqdm

data = open("day07.txt").read().strip()

# data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

data = [i.split(' ') for i in data.split('\n')]

print(data)
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# two different types of operators: add (+) and multiply (*)
def eval_expression(numbers, operators):
    res = numbers[0]
    for i, num in enumerate(numbers[1:]):
        op = operators[i]
        if op == '*':
            res *= numbers[i+1]
        else: # +
            res += numbers[i+1]
    return res

def generate_combos(n):
    if n <= 1:
        return [[]]
    combinations = []
    for smaller_combo in generate_combos(n - 1):
        combinations.append(smaller_combo + ['+'])
        combinations.append(smaller_combo + ['*'])
    return combinations

res = 0
for l in data:
    tar = int(l[0][:-1])
    r = [int(i) for i in l[1:]]
    combos = generate_combos(len(r))
    for combo in combos:
        if tar == eval_expression(r, combo):
            res += tar
            break



print("Part one: ")
print(res)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2
# concatenation operator (||)
def eval_expression2(numbers, operators):
    res = numbers[0]
    for i, num in enumerate(numbers[1:]):
        op = operators[i]
        if op == '*':
            res *= numbers[i+1]
        elif op == '+': # +
            res += numbers[i+1]
        else: # ||
            res = int(str(res) + str(numbers[i+1]))

    return res

def generate_combos2(n):
    if n <= 1:
        return [[]]
    combinations = []
    for smaller_combo in generate_combos2(n - 1):
        combinations.append(smaller_combo + ['+'])
        combinations.append(smaller_combo + ['*'])
        combinations.append(smaller_combo + ['||'])
    return combinations

res2 = 0
for l in tqdm(data, ncols=150):

    tar = int(l[0][:-1])
    r = [int(i) for i in l[1:]]
    combos = generate_combos2(len(r))
    for combo in combos:
        if tar == eval_expression2(r, combo):
            res2 += tar
            break

print("Part two: ")
print(res2)