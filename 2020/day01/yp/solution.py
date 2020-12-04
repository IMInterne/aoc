import os
import functools
import itertools


basedir = os.path.dirname(__file__)

with open(os.path.join(basedir, 'input.txt')) as f:
    data = [int(val) for val in f]

def solve(n):
    for combination in itertools.combinations(data, n):
        if sum(combination) == 2020:
            return functools.reduce(lambda x, y: x*y, combination)

print('Part 1...', solve(2))
print('Part 2...', solve(3))

