#!/usr/bin/env python
import re
import sys

hgt_cm_regex = re.compile(r'(\d+)cm')
hgt_in_regex = re.compile(r'(\d+)in')
def validate_hgt(hgt):
    match = hgt_cm_regex.fullmatch(hgt)
    if match:
        return 150 <= int(match.group(1)) <= 193
    match = hgt_in_regex.fullmatch(hgt)
    if match:
        return 59 <= int(match.group(1)) <= 76
    return False

hcl_regex = re.compile(r'#[a-f0-9]{6}')
valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
pid_regex = re.compile(r'\d{9}')
def validate_passport(passport):
    if not ('byr' in passport and (1920 <= int(passport['byr']) <= 2002)):
        return False

    if not ('iyr' in passport and (2010 <= int(passport['iyr']) <= 2020)):
        return False

    if not ('eyr' in passport and (2020 <= int(passport['eyr']) <= 2030)):
        return False

    if not ('hgt' in passport and validate_hgt(passport['hgt'])):
        return False

    if not ('hcl' in passport and hcl_regex.fullmatch(passport['hcl'])):
        return False

    if not ('ecl' in passport and passport['ecl'] in valid_ecl):
        return False

    if not ('pid' in passport and pid_regex.fullmatch(passport['pid'])):
        return False

    return True

regex = re.compile(r'(\S+):(\S+)')
valid_passports = 0
passport_field = {}
with open(sys.argv[1]) as f:
    for row in f:
        fields_groups = regex.findall(row)
        if fields_groups:
            passport_field.update({group[0]:group[1] for group in fields_groups})
        else:
            valid_passports += 1 if validate_passport(passport_field) else 0
            passport_field.clear() 
    valid_passports += 1 if validate_passport(passport_field) else 0
    print(valid_passports)

