def get_forms():
    form = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                yield form
                form = []
                continue
            form.append({c for c in line})
    yield form


print('Part 1:', sum(map(lambda sets: len(set().union(*sets)), get_forms())))
print('Part 2:', sum(map(lambda sets: len(set(sets[0]).intersection(*sets[1:])), get_forms())))
