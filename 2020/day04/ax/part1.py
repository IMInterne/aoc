import re


def validate_passport_from_batch(passport_batch_file_lines):
    passport_fields_regex = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):")
    valid_passport_count = 0
    current_fields = set()

    for line in passport_batch_file_lines:
        line = line.strip()
        if not line:
            number_of_fields = len(current_fields)
            if number_of_fields == 8 or (number_of_fields == 7 and "cid" not in current_fields):
                valid_passport_count += 1
            # reset passport
            current_fields = set()
            continue

        matching_fields = passport_fields_regex.findall(line)
        if matching_fields:
            current_fields = current_fields.union(set(matching_fields))

    number_of_fields = len(current_fields)
    if number_of_fields == 8 or (number_of_fields == 7 and "cid" not in current_fields):
        valid_passport_count += 1

    return valid_passport_count


if __name__ == '__main__':
    with open("data") as f:
        lines = f.readlines()

        valid_passport_count = validate_passport_from_batch(lines)
        print(valid_passport_count)
