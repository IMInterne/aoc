import itertools


def get_passports():
    pp = {}
    with open('input.txt') as f:
        for line in f:
            if not line.strip():
                yield pp
                pp = {}
                continue
            pp.update(dict(kws.split(':') for kws in line.split()))
    yield pp


def filter_part_one(pps):
    mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return [pp for pp in pps if not mandatory_keys - set(pp)]


def filter_part_two(pps):
    valid_byr = lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002
    valid_iyr = lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020
    valid_eyr = lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030
    valid_hgt = lambda hgt: (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76)
    valid_hcl = lambda hcl: hcl[0] == '#' and len(hcl[1:]) == 6 and not set(hcl[1:]) - set(itertools.chain(map(str, range(10)), map(chr, range(97, 103))))
    valid_ecl = lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    valid_pid = lambda pid: len(pid) == 9 and not set(pid) - set(map(str, range(10)))
    return [
        pp for pp in pps if valid_byr(pp['byr']) and valid_iyr(pp['iyr']) and valid_eyr(pp['eyr'])
        and valid_hgt(pp['hgt']) and valid_hcl(pp['hcl']) and valid_ecl(pp['ecl']) and valid_pid(pp['pid'])]


part_one = filter_part_one(get_passports())
print('Part 1: ', len(part_one))
print('Part 2: ', len(filter_part_two(part_one)))
