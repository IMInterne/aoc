with open('input.txt') as f:
    data = [line for line in f]


def get_boarding_ids():
    for boarding in data:
        row = ''.join(map(lambda l: '0' if l == 'F' else '1', boarding[:7]))
        column = ''.join(map(lambda l: '0' if l == 'L' else '1', boarding[7:10]))
        yield int(row, 2) * 8 + int(column, 2)


boardings = set(get_boarding_ids())
print('Part 1:', max(boardings))
print('Part 2:', set(range(min(boardings), max(boardings))) - boardings)
