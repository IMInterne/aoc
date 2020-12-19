class Bag:
    def __init__(self, color, children=None):
        self.color = color
        self.children = children or {}

    def add_child(self, *children):
        for child in children:
            color = []
            number = 0
            for c in child:
                if c.isdigit():
                    number = int(c)
                else:
                    color.append(c)
            self.children[''.join(color).strip()] = number

    def __hash__(self):
        return hash(self.color)

    def __eq__(self, other):
        return str(other) == self.color

    def __contains__(self, other):
        return str(other) in self.children

    def __repr__(self):
        return '{}->{}'.format(self.color, self.children)
    
    def __str__(self):
        return self.color


def get_bags():
    with open('input.txt') as f:
        for line in f:
            p, c = line.split('contain')
            parent = Bag(p.rstrip(' bags'))
            children = [p_child for child in c.strip().split(',') if (p_child := child.strip('.').rstrip(' bags').strip()) != 'no other']
            parent.add_child(*children)
            yield parent


bags = list(get_bags())


def can_contain(colors):
    found = {bag for bag in bags if any(map(lambda color: color in bag, colors))}
    if not found:
        return set()
    return found | can_contain(found)


def contained_in(color, times):
    found = [bag for bag in bags if bag == color]
    bag = found.pop()
    if not bag.children:
        return 0
    direct_children = (sum(bag.children.values()) + sum(contained_in(c, t) for c, t in bag.children.items())) * times
    return direct_children


print('Part 1:', len(can_contain(['shiny gold'])))
print('Part 2:', contained_in('shiny gold', times=1))
