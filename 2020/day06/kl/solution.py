

if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        groups = data.split("\n\n")
        s = 0
        for group in groups:
            group_answers = set("abcdefghijklmnopqrstuvwxyz")
            for answers in group.split("\n"):
                group_answers &= set(answers.strip())
            s += len(group_answers)
        print(s)
