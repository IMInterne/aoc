ROW_LENGTH = 31


def _is_tree(value):
    return value == "#"


def count_trees(current_x, current_y, slope_map):
    total_trees = 0
    total_height = len(slope_map)

    while current_y < total_height - 1:
        current_x, current_y, encountered_trees = move(current_x, current_y, slope_map)
        print(f"{current_x}, {current_y} {encountered_trees}")
        total_trees += encountered_trees

    return total_trees


def move(current_x, current_y, slope_map):
    traversed_trees = 0
    current_x += 3

    if current_x > ROW_LENGTH - 1:
        current_x = current_x - 31

    current_y += 1
    if _is_tree(slope_map[current_y][current_x]):
        traversed_trees += 1

    return current_x, current_y, traversed_trees


if __name__ == '__main__':
    with open("data") as f:
        grid = [slope.strip() for slope in f.readlines()]
        print(count_trees(0, 0, grid))
