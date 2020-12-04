import functools
import itertools
import pathlib


def product_of_sum_that_equals(s, numbers, n):
    for a in itertools.combinations(numbers, n):
        if sum(a) == s:
            print(functools.reduce(lambda x, y: x*y, a))
            break


if __name__ == '__main__':
    input_file = pathlib.Path('input.txt')
    with input_file.open() as f:
        numbers = [int(n) for n in f]
    product_of_sum_that_equals(2020, numbers, 2)
    product_of_sum_that_equals(2020, numbers, 3)
