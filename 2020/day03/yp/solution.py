with open('input.txt') as f:
    data = [line.strip() for line in f]


def solve(right, down):
    i = 0
    trees = 0
    for line in data[::down]:
        if line[i % len(line)] == '#':
            trees += 1
        i += right
    return trees


print(solve(3, 1))
print(solve(3, 1) * solve(1, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
