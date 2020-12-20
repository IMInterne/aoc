import itertools


with open('input.txt') as f:
    data = [int(line.strip()) for line in f]


def get_invalid_number():
    for i, number in enumerate(data[25:], start=25):
        for comb in itertools.combinations(data[i-25:i], 2):
            if sum(comb) == number:
                break
        else:
            return number


def find_weakness(invalid_num):
    begin = 0
    end = 2
    while True:
        comb = data[begin:end]
        result = sum(comb)
        if result == invalid_num:
            return max(comb) + min(comb)
        elif result > invalid_num:
            begin += 1
            end = begin + 2
        else:
            end += 1


invalid_num = get_invalid_number()
print('Part 1:', invalid_num)
print('Part 2:', find_weakness(invalid_num))
