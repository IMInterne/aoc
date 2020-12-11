
if __name__ == '__main__':
    with open("input_test.txt") as f:
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
    print(sum((not (required_fields - set(passport)) for passport in passport_dicts)))
