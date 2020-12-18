import re


required_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }


def is_valid_hgt(hgt):
    if "cm" in hgt:
        return 150 <= int(hgt.strip("cm")) <= 193
    if "in" in hgt:
        return 59 <= int(hgt.strip("in")) <= 76


def is_valid(passport):
    if required_fields <= set(passport):
        validation_tuple = (
                1920 <= int(passport["byr"]) <= 2002,
                2010 <= int(passport["iyr"]) <= 2020,
                2020 <= int(passport["eyr"]) <= 2030,
                is_valid_hgt(passport["hgt"]),
                re.fullmatch("#[0-9a-z]{6}", passport["hcl"]),
                passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                re.fullmatch("\d{9}", passport["pid"])
            )
        print(validation_tuple)
        return all(validation_tuple)
    return False


if __name__ == '__main__':
    with open("input.txt") as f:
        passports = f.read().split("\n\n")
    passport_dicts = []
    for passport_str in passports:
        passport_str = passport_str.replace("\n", " ")
        passport_dict = {}
        for info in passport_str.split(" "):
            key, value = info.split(":")
            passport_dict[key] = value
        passport_dicts.append(passport_dict)

    required_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }
    print(sum(is_valid(passport) for passport in passport_dicts))
