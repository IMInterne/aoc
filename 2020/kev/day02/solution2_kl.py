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
            first_pos, second_pos = (int(i)-1 for i in rule.split("-"))
            letter = letter.strip(':')
            char_checks = (password[first_pos] == letter, password[second_pos] == letter)
            if any(char_checks) and not all(char_checks):
                count += 1
    print(count)
