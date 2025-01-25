import sys
input = sys.stdin
output = sys.stdout


def main():
    count_input_data = int(input.readline().strip())
    for _ in range(count_input_data):
        size_str = input.readline().strip().split()
        n, m = int(size_str[0]), int(size_str[1])
        field = [list(input.readline().strip()) for _ in range(n)]
        result = get_modified_field(n, m, field)
        for row in result:
            output.write("".join(row) + "\n")


def get_modified_field(n, m, field):
    coords = find_positions(n, m, field)

    # Если робот A сверху или на одной строке с B
    if coords[0][0] < coords[1][0]:
        return paint_path(field, coords[0][0], coords[0][1], coords[1][0], coords[1][1], n, m, 'a', 'b')
    elif coords[0][0] == coords[1][0] and coords[0][1] > coords[1][1]:
        return paint_path(field, coords[1][0], coords[1][1], coords[0][0], coords[0][1], n, m, 'b', 'a')
    elif coords[0][0] == coords[1][0] and coords[0][1] < coords[1][1]:
        return paint_path(field, coords[0][0], coords[0][1], coords[1][0], coords[1][1], n, m, 'a', 'b')
    else:
        return paint_path(field, coords[1][0], coords[1][1], coords[0][0], coords[0][1], n, m, 'b', 'a')


def paint_path(field, coord_x_up, coord_y_up, coord_x_down, coord_y_down, n, m, up_marker, down_marker):
    # Робот верхний
    if coord_y_up % 2 != 0:
        coord_y_up -= 1
        field[coord_x_up][coord_y_up] = up_marker

    for i in range(coord_x_up - 1, -1, -1):
        field[i][coord_y_up] = up_marker

    for j in range(coord_y_up - 1, -1, -1):
        field[0][j] = up_marker

    # Робот нижний
    if coord_y_down % 2 != 0:
        coord_y_down += 1
        field[coord_x_down][coord_y_down] = down_marker

    for i in range(coord_x_down + 1, n):
        field[i][coord_y_down] = down_marker

    for j in range(coord_y_down + 1, m):
        field[n - 1][j] = down_marker

    return field


def find_positions(n, m, field):
    is_find_a = False
    is_find_b = False
    coords = [[0, 0], [0, 0]]

    for i in range(n):
        for j in range(m):
            if i % 2 != 0 and j % 2 != 0:
                continue
            if not is_find_a and field[i][j] == 'A':
                coords[0] = [i, j]
                is_find_a = True
            if not is_find_b and field[i][j] == 'B':
                coords[1] = [i, j]
                is_find_b = True
            if is_find_a and is_find_b:
                return coords

    return coords


if __name__ == "__main__":
    main()
