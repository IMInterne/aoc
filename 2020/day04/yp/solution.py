import itertools


def get_passwords():
    pw = {}
    with open('input.txt') as f:
        for line in f:
            if not line.strip():
                yield pw
                pw = {}
                continue
            pw.update(dict(kws.split(':') for kws in line.split()))
    yield pw


def filter_part_one(pws):
    mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return [pw for pw in pws if not mandatory_keys - set(pw)]


def filter_part_two(pws):
    valid_byr = lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002
    valid_iyr = lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020
    valid_eyr = lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030
    valid_hgt = lambda hgt: (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76)
    valid_hcl = lambda hcl: hcl[0] == '#' and len(hcl[1:]) == 6 and not set(hcl[1:]) - set(itertools.chain(map(str, range(10)), map(chr, range(97, 103))))
    valid_ecl = lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    valid_pid = lambda pid: len(pid) == 9 and not set(pid) - set(map(str, range(10)))
    return [
        pw for pw in pws if valid_byr(pw['byr']) and valid_iyr(pw['iyr']) and valid_eyr(pw['eyr'])
        and valid_hgt(pw['hgt']) and valid_hcl(pw['hcl']) and valid_ecl(pw['ecl']) and valid_pid(pw['pid'])]


part_one = filter_part_one(get_passwords())
print('Part 1: ', len(part_one))
print('Part 2: ', len(filter_part_two(part_one)))
