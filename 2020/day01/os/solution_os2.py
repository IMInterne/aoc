#!/usr/bin/env python3
import itertools
import sys

numbers = []

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        numbers.append(int(line))

for (numberA, numberB, numberC) in itertools.product(numbers, repeat=3):
    if numberA == numberB or numberA == numberC or numberB == numberC:
        continue
    if numberA + numberB + numberC == 2020:
        print("{} * {} * {} = {}".format(numberA, numberB, numberC, numberA * numberB * numberC))
        break
