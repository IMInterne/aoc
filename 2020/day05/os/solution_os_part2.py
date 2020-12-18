#!/usr/bin/env python
import copy
import sys

seats_ids = set()
for row in range(1,112):
    for column in range(8):
        seats_ids.add(row * 8 + column)
full_seats_ids = copy.copy(seats_ids)
print("Seats ids : ", seats_ids)
print("Seats ids count : ", len(seats_ids))


with open(sys.argv[1]) as f:
    for line in f:
        row = line[0:7]
        row = row.replace('F', '0').replace('B', '1')
        row = int(row, 2)
        column = line[7:10]
        column = column.replace('R', '1').replace('L', '0')
        column = int(column, 2)
        seat_id = row * 8 + column
        print("seat_id : ", seat_id)
        if seat_id in seats_ids:
            seats_ids.remove(seat_id)
print("My seat id : ", seats_ids)

