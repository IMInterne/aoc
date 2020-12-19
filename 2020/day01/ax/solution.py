SUM_SOLUTION = 2020


def _find_sum(wanted_sum, possible_numbers):
    first_number = possible_numbers[0]
    last_number = possible_numbers[-1]

    if last_number == first_number:
        # single element remains, no solution
        return False, (0, 0)

    result = first_number + last_number
    if result == wanted_sum:
        # found solution
        return True, (first_number, last_number)

    if result > wanted_sum:
        # busted wanted sum, discard last number and retry for a new solution
        return _find_sum(wanted_sum, possible_numbers[0:-1])

    # first number is too low, try again with the next one
    return _find_sum(wanted_sum, possible_numbers[1:])


if __name__ == '__main__':
    with open("data") as f:
        numbers = [int(n) for n in f.readlines()]
        print(_find_sum(SUM_SOLUTION, sorted(numbers)))
