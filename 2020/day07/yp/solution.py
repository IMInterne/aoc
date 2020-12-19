import itertools


class Bag:
    def __init__(self, color, children=None):
        self.color = color
        self.children = children or []

    def add_child(self, *child):
        self.children.append(child)

    def __hash__(self):
        return hash(self.color)

    def __eq__(self, other):
        return other in self.color

    def __contains__(self, other):
        return any(map(lambda color: other in color, self.children))

    def __repr__(self):
        return '{}->{}'.format(self.color, self.children)


def get_bags():
    with open('input.txt') as f:
        for line in f:
            p, c = line.split('contain')
            parent = Bag(p.rstrip(' bags'))
            children = [''.join(letter for letter in child.strip('.').rstrip(' bags') if not letter.isdigit()).strip() for child in c.strip().split(',')]
            parent.add_child(*children)
            yield parent


bags = list(get_bags())


def can_contain(colors):
    found = {bag for bag in bags if any(map(lambda color: color in bag, colors))}
    if not found:
        return set()
    return found | can_contain(found)


def contain(colors):
    found = {bag for bag in bags if any(map(lambda color: bag == color, colors))}
    if not found:
        return set()
    children = set(itertools.chain(*[c for bag in found for c in bag.children]))
    return children | contain(children)


print('Part 1:', len(can_contain(['shiny gold'])))
