#!/usr/bin/env python3
import itertools
import sys

j = 0
trees = 0
rows = []
with open(sys.argv[1]) as f:
    for row in f:
        # Il faut enlever le \n à la fin. C'est pour ça qu'on fait -1.
        trees += 1 if row[j % (len(row)-1)] == '#' else 0
        j += 3
print("Number of trees : ", trees)
