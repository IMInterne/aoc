ROW_LENGTH = 31
SLOPE_COUNT = 323


def _is_tree(value):
    return value == "#"


def count_trees(current_x, current_y, slope_map, x_speed, y_speed):
    total_trees = 0
    total_height = len(slope_map)

    while current_y < total_height - 1:
        current_x, current_y, encountered_trees = move(current_x, current_y, slope_map, x_speed, y_speed)
        print(f"{current_x}, {current_y} {encountered_trees}")
        total_trees += encountered_trees

    return total_trees


def move(current_x, current_y, slope_map, x_speed, y_speed):
    traversed_trees = 0
    current_x += x_speed

    if current_x > ROW_LENGTH - 1:
        current_x = current_x - 31

    current_y += y_speed
    if current_y > SLOPE_COUNT - 1:
        # cannot bust
        current_y = SLOPE_COUNT - 1

    if _is_tree(slope_map[current_y][current_x]):
        traversed_trees += 1

    return current_x, current_y, traversed_trees


if __name__ == '__main__':
    result = 1
    with open("data") as f:
        grid = [slope.strip() for slope in f.readlines()]
        for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            number_of_trees = count_trees(0, 0, grid, x, y)
            print(f"Encountered {number_of_trees} trees.")
            result = result * number_of_trees

    print(f"Result is: {result}")
