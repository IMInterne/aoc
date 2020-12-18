#!/usr/bin/env python
import sys

seats_ids = []
with open(sys.argv[1]) as f:
    for line in f:
        row = line[0:7]
        row = row.replace('F', '0').replace('B', '1')
        row = int(row, 2)
        print("row : ", row)
        column = line[7:10]
        column = column.replace('R', '1').replace('L', '0')
        column = int(column, 2)
        print("column : ", column)
        seat_id = row * 8 + column
        seats_ids.append(seat_id)
        print("id : ", seat_id)
print("Max seat id : ", max(seats_ids))

