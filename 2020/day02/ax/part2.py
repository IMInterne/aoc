import re


def count_valid_password(data):
    policies_and_passwords = [line.strip() for line in data.splitlines() if line]

    policy_and_password_re = re.compile("(?P<min>\d+)-(?P<max>\d+) (?P<char>.): (?P<password>.+)")

    total_matching_password = 0

    for password_and_policy in policies_and_passwords:
        match = policy_and_password_re.match(password_and_policy)

        if match:
            result = match.groupdict()
            char_ = result.get("char")
            first_position = int(result.get("min"))
            second_position = int(result.get("max"))

            password = result.get("password")

            first_match = password[first_position - 1] == char_
            second_match = password[second_position - 1] == char_

            if (first_match and not second_match) or (second_match and not first_match):
                total_matching_password += 1
        else:
            raise Exception(f"Received unknown stuff {password_and_policy}")

    return total_matching_password


if __name__ == '__main__':
    with open("data") as f:
        policies_and_passwords_raw = f.read()
        print(count_valid_password(policies_and_passwords_raw))
