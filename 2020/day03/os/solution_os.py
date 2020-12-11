#!/usr/bin/env python3
import itertools
import sys

j = 0
trees_r1d1 = 0
with open(sys.argv[1]) as f:
    for row in f:
        # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
        trees_r1d1 += 1 if row[j % (len(row)-1)] == '#' else 0
        j += 1
print("Number of trees Right 1, Down 1 : ", trees_r1d1)

j = 0
trees_r3d1 = 0
with open(sys.argv[1]) as f:
    for row in f:
        # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
        trees_r3d1 += 1 if row[j % (len(row)-1)] == '#' else 0
        j += 3
print("Number of trees Right 3, Down 1 : ", trees_r3d1)

j = 0
trees_r5d1 = 0
with open(sys.argv[1]) as f:
    for row in f:
        # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
        trees_r5d1 += 1 if row[j % (len(row)-1)] == '#' else 0
        j += 5
print("Number of trees Right 5, Down 1 : ", trees_r5d1)

j = 0
trees_r7d1 = 0
with open(sys.argv[1]) as f:
    for row in f:
        # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
        trees_r7d1 += 1 if row[j % (len(row)-1)] == '#' else 0
        j += 7
print("Number of trees Right 7, Down 1 : ", trees_r7d1)

i = 0
j = 0
trees_r1d2 = 0
with open(sys.argv[1]) as f:
    for row in f:
        if (i % 2) == 0:
            # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
            trees_r1d2 += 1 if row[j % (len(row)-1)] == '#' else 0
            j += 1
        i += 1
print("Number of trees Right 1, Down 2 : ", trees_r1d2)

print("Total number of trees", trees_r1d1 * trees_r3d1 * trees_r5d1 * trees_r7d1 * trees_r1d2)
