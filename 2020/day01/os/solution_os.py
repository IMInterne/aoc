#!/usr/bin/env python3
import itertools
import sys

numbers = []

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        numbers.append(int(line))

for (numberA, numberB) in itertools.product(numbers, repeat=2):
    if numberA + numberB == 2020:
        print("{} * {} = {}".format(numberA, numberB, numberA * numberB))
        break
