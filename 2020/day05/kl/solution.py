
def to_int(string_: str, bitmap):
    bin_num = string_
    for letter, repr_ in bitmap.items():
        bin_num = bin_num.replace(letter, repr_)
    return int(bin_num, 2)


if __name__ == '__main__':
    row_map = {"F": "0", "B": "1"}
    column_map = {"L": "0", "R": "1"}
    used_seats = []
    with open("input.txt") as f:
        for line in f:
            row = to_int(line.strip()[:-3], row_map)
            column = to_int(line.strip()[-3:], column_map)
            used_seats.append(row * 8 + column)
    used_seats.sort()
    print(used_seats[-1])
    for i, j in zip(used_seats, used_seats[1:]):
        if j - i != 1:
            print(i + 1)
            break
