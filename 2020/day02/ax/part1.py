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
            min_ = int(result.get("min"))
            max_ = int(result.get("max"))

            password = result.get("password")
            occurrence = password.count(char_)

            if min_ <= occurrence <= max_:
                total_matching_password += 1
        else:
            raise Exception(f"Receive unknown stuff {password_and_policy}")

    return total_matching_password


if __name__ == '__main__':
    with open("data") as f:
        everything = f.read()
        print(count_valid_password(everything))
