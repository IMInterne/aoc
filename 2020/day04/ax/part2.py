import re


class ValidationRule(object):
    def validate(self, value):
        pass


class NoValidationRule(ValidationRule):
    def validate(self, value):
        return True


class MinMaxValidation(ValidationRule):
    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

    def validate(self, value):
        if not isinstance(value, int):
            value = int(value)

        return self._min <= value <= self._max


class HeightValidation(ValidationRule):
    def __init__(self):
        self._regex = re.compile("(?P<height>\d+)(?P<uom>(cm|in))")
        self._uom_validator = {
            "cm": MinMaxValidation(150, 193),
            "in": MinMaxValidation(59, 76)
        }

    def validate(self, value):
        match = self._regex.search(value)
        if not match:
            return False

        groups = match.groupdict()
        uom = groups.get("uom")
        value = groups.get("height")

        # defaults to invalid validation
        validator = self._uom_validator.get(uom, lambda v: False)
        return validator.validate(value)


class RegexValidator(ValidationRule):
    def __init__(self, regex_pattern):
        self._regex = re.compile(regex_pattern)

    def validate(self, value):
        match = self._regex.search(value)
        if not match:
            return False
        # match found
        return True


class Passport(object):
    def __init__(self):
        self._fields = {}

    def add(self, field_name, field_value):
        self._fields[field_name] = field_value

    def get_field(self, name):
        return self._fields.get(name)


class PassportValidator(object):
    def __init__(self):
        self._fields_validator = {
            "byr": MinMaxValidation(1920, 2002),
            "iyr": MinMaxValidation(2010, 2020),
            "eyr": MinMaxValidation(2020, 2030),
            "hgt": HeightValidation(),
            "hcl": RegexValidator("#([0-9]|[a-f]){6}"),
            "ecl": RegexValidator("(amb|blu|brn|gry|grn|hzl|oth)"),
            "pid": RegexValidator(r"\d{9}"),
            "cid": NoValidationRule(),
        }

    def validate(self, passport):
        for field_name, validator in self._fields_validator.items():
            field_value = passport.get_field(field_name)
            if not field_value and field_name != "cid":
                return False

            if not validator.validate(field_value):
                return False

            # go to next field

        return True


def validate_passport_from_batch(passport_batch_file_lines):
    passport_fields_regex = re.compile(r"(?P<field_name>(byr|iyr|eyr|hgt|hcl|ecl|pid|cid)):(?P<value>\S+)")
    valid_passport_count = 0
    passport_validator = PassportValidator()

    current_passport = Passport()

    for line in passport_batch_file_lines:
        line = line.strip()
        if not line:
            if passport_validator.validate(current_passport):
                valid_passport_count += 1
            # reset passport
            current_passport = Passport()
            continue

        for match in passport_fields_regex.finditer(line):
            result = match.groupdict()
            current_passport.add(result.get("field_name"), result.get("value"))

    if passport_validator.validate(current_passport):
        valid_passport_count += 1

    return valid_passport_count


if __name__ == '__main__':
    with open("data") as f:
        lines = f.readlines()
        print(validate_passport_from_batch(lines))
