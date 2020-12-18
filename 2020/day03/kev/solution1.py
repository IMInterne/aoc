class RepeatableRow:
    def __init__(self, row, repeat=100):
        self.row = row
        self.repeat = repeat

    def __getitem__(self, i: int):
        return self.row[i % len(self.row)]

    def __len__(self):
        return len(self.row) * self.repeat


class Slope:
    def __init__(self, map_, right, down):
        self.map = map_
        self.right = right
        self.down = down

    @classmethod
    def from_input(cls, input_file_path, right, down):
        with open(input_file_path) as f:
            map_ = [RepeatableRow(line.strip()) for line in f]
        return cls(map_, right, down)

    def __getitem__(self, i):
        return self.map[self.down * i][self.right * i]

    def __len__(self):
        return len(self.map) / self.down


if __name__ == '__main__':
    a11 = sum(s == "#" for s in Slope.from_input("input.txt", 1, 1))
    a31 = sum(s == "#" for s in Slope.from_input("input.txt", 3, 1))
    a51 = sum(s == "#" for s in Slope.from_input("input.txt", 5, 1))
    a71 = sum(s == "#" for s in Slope.from_input("input.txt", 7, 1))
    a12 = sum(s == "#" for s in Slope.from_input("input.txt", 1, 2))
    print(a31)
    print(a11*a31*a51*a71*a12)
