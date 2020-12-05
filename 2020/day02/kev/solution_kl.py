import pathlib

def count_chars(string, char_):
    count = 0
    for c in string:
        if c == char_:
            count += 1
    return count


if __name__ == '__main__':
    input_file = pathlib.Path('input.txt')
    with input_file.open() as f:
        count = 0
        for l in f:
            rule, letter, password = l.split(" ")
            rule_min, rule_max = (int(i) for i in rule.split("-"))
            letter = letter.strip(':')
            if rule_min <= count_chars(password, letter) <= rule_max:
                count += 1
    print(count)
