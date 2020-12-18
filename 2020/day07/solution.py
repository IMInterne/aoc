import re

phrase_regex = re.compile(r"(?P<bag>[a-z ]+) bags contain (?P<contains>.*).")
contains_regex = re.compile(r"(?P<n>\d+) (?P<bag>.*) bag")


class Bag:
    def __init__(self, name):
        self.name = name
        self._contain_bag = {}

    def __hash__(self):
        return self.name

    def __getitem__(self, item):
        return self._contain_bag[item]

    def __iter__(self):
        return self._contain_bag

    def __len__(self):
        return len(self._contain_bag)


def parse_phrase(phrase):
    group_phrase = phrase_regex.match(phrase)
    bag = group_phrase.groupdict()["bag"]
    contains = []
    for contain_bag in group_phrase.groupdict()["contains"].split(", "):
        group_contain_bag = contains_regex.match(contain_bag)
        contains.append((group_contain_bag.groupdict()["n"], group_contain_bag.groupdict()["bag"]))
    return bag, contains


if __name__ == '__main__':
    print(parse_phrase("bright bronze bags contain 1 clear magenta bag, 2 clear gray bags, 2 dull coral bags, 5 vibrant gray bags."))
