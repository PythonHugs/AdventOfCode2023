""" Part 2 for Puzzle 11 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/11
import itertools


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def make_puzzle_list(puzzle_input):
    listed_puzzle_input = [list(line) for line in puzzle_input]
    return listed_puzzle_input


def find_empty_columns(puzzle_input):
    expanded_cols_index = []
    row_length = len(puzzle_input[0])
    col_length = len(puzzle_input)
    for i in range(row_length):
        is_col_empty = True
        for j in range(col_length):
            if puzzle_input[j][i] != '.':
                is_col_empty = False
                break
        if is_col_empty:
            expanded_cols_index.append(i)
    return expanded_cols_index


def find_empty_rows(puzzle_input):
    expanded_rows_index = []
    row_length = len(puzzle_input[0])
    empty_row = ['.' for _ in range(row_length)]
    for i, row in enumerate(puzzle_input):
        if row == empty_row:
            expanded_rows_index.append(i)
    print(len(expanded_rows_index))
    return expanded_rows_index


def print_grid(puzzle_input):
    for row in puzzle_input:
        str_row = [str(i) for i in row]
        print(''.join(str_row))
    print('')


def number_galaxies(puzzle_input):
    current_number = 1
    for i, row in enumerate(puzzle_input):
        for j, column in enumerate(row):
            if column == '#':
                puzzle_input[i][j] = current_number
                current_number += 1
    return puzzle_input, current_number


def generate_pairs(n):
    return list(itertools.combinations(range(1, n), 2))


def calc_distance(coords_1, coords_2, expanded_rows, expanded_columns):
    expansion_factor = 1000000  # One million as per problem's rules

    # Identify the range of rows/columns travelled
    travelled_rows = range(min(coords_1[0], coords_2[0]), max(coords_1[0], coords_2[0]) + 1)
    travelled_columns = range(min(coords_1[1], coords_2[1]), max(coords_1[1], coords_2[1]) + 1)

    # Identify which of these are empty
    empty_rows_travelled = set(travelled_rows).intersection(expanded_rows)
    empty_columns_travelled = set(travelled_columns).intersection(expanded_columns)

    # Calculate the distance
    row_distance = abs(coords_1[0] - coords_2[0]) + len(empty_rows_travelled) * (expansion_factor - 1)
    col_distance = abs(coords_1[1] - coords_2[1]) + len(empty_columns_travelled) * (expansion_factor - 1)

    return row_distance + col_distance


def get_pair_coords(pair, puzzle_input):
    col_length = len(puzzle_input)
    pair_coords = []
    for n in pair:
        for i in range(col_length):
            try:
                c = (i, puzzle_input[i].index(n))
            except ValueError:
                continue
        pair_coords.append(c)
    return pair_coords


def main(puzzle_input):
    # print(puzzle_input)

    puzzle_input = make_puzzle_list(puzzle_input)
    print_grid(puzzle_input)
    print(len(puzzle_input))

    expanded_columns_index = find_empty_columns(puzzle_input)
    expanded_rows_index = find_empty_rows(puzzle_input)

    puzzle_input, gal_num = number_galaxies(puzzle_input)
    # alt_puzzle, gal_num = number_galaxies(original_puzzle)
    print_grid(puzzle_input)

    gal_pairs = generate_pairs(gal_num)
    print(gal_pairs)
    print(len(gal_pairs))
    print('')

    pair_coords = []
    for pair in gal_pairs:
        pc = get_pair_coords(pair, puzzle_input)
        pair_coords.append(pc)
    print(pair_coords)
    print(len(pair_coords))
    print('')

    distances = []
    for coords in pair_coords:
        distance = calc_distance(coords[0], coords[1], expanded_rows_index, expanded_columns_index)
        distances.append(distance)
    print(distances)
    print(len(distances))
    print('')

    print(sum(distances))


if __name__ == '__main__':
    # puzzle_input = read_input('part_2_puzzle_11_example_input.txt')
    puzzle_input = read_input('part_2_puzzle_11_input.txt')
    main(puzzle_input)
