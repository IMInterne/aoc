#!/usr/bin/env python3
import collections
import re
import sys

PasswordValidation = collections.namedtuple("PasswordValidation", ["min", "max", "letter", "password"])
validations = []

regex = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)")

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        match = regex.match(line)
        if match:
            validations.append(PasswordValidation(int(match.group('min')), int(match.group('max')), match.group('letter'), match.group('password')))

valid_passwords_part1 = []
valid_passwords_part2 = []
for v in validations:
    count_letter = v.password.count(v.letter)
    print(v.min, v.max, v.letter, v.password, count_letter)
    if count_letter >= v.min and count_letter <= v.max:
        print("password is valid for part1")
        valid_passwords_part1.append(v.password)
    if (v.password[v.min-1] == v.letter) != (v.password[v.max-1] == v.letter):
        print("password is valid for part2")
        valid_passwords_part2.append(v.password)

print("Number of valid passwords for part 1: ", len(valid_passwords_part1))
print("Number of valid passwords for part 2: ", len(valid_passwords_part2))
