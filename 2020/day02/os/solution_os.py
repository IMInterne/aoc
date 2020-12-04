#!usr/bin/env python3
import collections
import re
import sys

PasswordValidation = collections.namedtuple("PasswordValidation", ["min", "max", "letter", "password"])
validations = []

regex = re.compile("(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)")

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        match = regex.match(line)
        if match:
            validations.append(PasswordValidation(int(match.group('min')), int(match.group('max')), match.group('letter'), match.group('password')))

valid_passwords_part1 = []
valid_passwords_part2 = []
for validation in validations:
    count_letter = validation.password.count(validation.letter)
    print(validation.min, validation.max, validation.letter, validation.password, count_letter)
    if count_letter >= validation.min and count_letter <= validation.max:
        print("password is valid for part1")
        valid_passwords_part1.append(validation.password)
    if (validation.password[validation.min-1] == validation.letter) != (validation.password[validation.max-1] == validation.letter):
        print("password is valid for part2")
        valid_passwords_part2.append(validation.password)

print("Number of valid passwords for part 1: ", len(valid_passwords_part1))
print("Number of valid passwords for part 2: ", len(valid_passwords_part2))
