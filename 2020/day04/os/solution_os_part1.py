#!/usr/bin/env python
import re
import sys

regex = re.compile(r'(\S+):(\S+)')
valid_passports = 0
must_have_field = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport_field = {}
with open(sys.argv[1]) as f:
    for row in f:
        fields_groups = regex.findall(row)
        if fields_groups:
            passport_field.update({group[0]:group[1] for group in fields_groups})
        else:
            valid_passports += 1 if (set(passport_field.keys()) >= must_have_field) else 0
            passport_field.clear() 
    valid_passports += 1 if (set(passport_field.keys()) >= must_have_field) else 0
    print(valid_passports)
