import os

basedir = os.path.dirname(__file__)


class PlomberieMixin:
    @classmethod
    def from_raw_input(cls, raw_input):
        condition, letter = raw_input.split(' ')
        return cls(letter, *map(int, condition.split('-')))


class RulePart1(PlomberieMixin):
    def __init__(self, letter: str, min_occurence: int, max_occurence: int):
        self.letter = letter
        self.min_occ = min_occurence
        self.max_occ = max_occurence

    def verify(self, password: str):
        return self.min_occ <= password.count(self.letter) <= self.max_occ


class RulePart2(PlomberieMixin):
    def __init__(self, letter: str, position_one: int, position_two: int):
        self.letter = letter
        self.positions = {position_one, position_two}

    def verify(self, password: str):
        return len(self.positions - {i for i, letter in enumerate(password, start=1) if letter == self.letter}) == 1


valid_pw_1 = []
valid_pw_2 = []
with open(os.path.join(basedir, 'input.txt')) as f:
    for raw_i in f:
        rule_input, password = raw_i.split(':')
        password = password.strip()
        if RulePart1.from_raw_input(rule_input).verify(password):
            valid_pw_1.append(password)
        if RulePart2.from_raw_input(rule_input).verify(password):
            valid_pw_2.append(password)
print('Part 1: ', len(valid_pw_1))
print('Part 2: ', len(valid_pw_2))
