""" Part 2 for Puzzle 11 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/11
import itertools
import copy


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


def expand_empty_columns(puzzle_input):
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
    offset = 0
    print(len(expanded_cols_index))
    for ex_col in expanded_cols_index:
        for i in range(col_length):
            puzzle_input[i] = puzzle_input[i][:ex_col + offset] + ['W'] + puzzle_input[i][ex_col + offset:]
        offset += 1
    print_grid(puzzle_input)

    for i in range(row_length):
        for j in range(col_length):
            if puzzle_input[j][i] == 'W':
                puzzle_input[j][i] = '.'
    return puzzle_input, expanded_cols_index


def expand_empty_rows(puzzle_input):
    expanded_rows_index = []
    row_length = len(puzzle_input[0])
    empty_row = ['.' for _ in range(row_length)]
    alt_row = ['W' for _ in range(row_length)]
    alt_row2 = ['O' for _ in range(row_length)]
    for i, row in enumerate(puzzle_input):
        if row == empty_row:
            expanded_rows_index.append(i)
            puzzle_input[i] = alt_row2
            puzzle_input.insert(i, alt_row)
    print(len(expanded_rows_index))
    print_grid(puzzle_input)

    for i, row in enumerate(puzzle_input):
        if row == alt_row or row == alt_row2:
            puzzle_input[i] = empty_row
    return puzzle_input, expanded_rows_index


def expand_grid(puzzle_input):
    puzzle_input, expanded_rows_index = expand_empty_rows(puzzle_input)
    puzzle_input, expanded_columns_index = expand_empty_columns(puzzle_input)
    return puzzle_input, expanded_rows_index, expanded_columns_index


def print_grid(puzzle_input):
    for row in puzzle_input:
        # print(row)
        print(''.join(row))
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


def calc_distance(coords_1, coords_2):
    return abs(coords_1[0] - coords_2[0]) + abs(coords_1[1] - coords_2[1])


def get_pair_coords(pair, puzzle_input, expanded_columns_index, expanded_rows_index):
    col_length = len(puzzle_input)
    row_length = len(puzzle_input[0])
    pair_coords = []
    empty_row_counter = 0
    empty_column_counter = 0
    expansion = 10
    for n in pair:
        for i in range(col_length):
            if i in expanded_columns_index:
                empty_column_counter += expansion
            for j in range(row_length):
                if j in expanded_rows_index:
                    empty_row_counter += expansion
                if puzzle_input[i][j] == n:
                    c = (i + empty_column_counter, j + empty_row_counter)
        pair_coords.append(c)
        empty_column_counter = empty_row_counter = 0
    return pair_coords


def main(puzzle_input):
    # print(puzzle_input)

    puzzle_input = make_puzzle_list(puzzle_input)
    print_grid(puzzle_input)
    print(len(puzzle_input))

    original_puzzle = copy.deepcopy(puzzle_input)

    puzzle_input, expanded_rows_index, expanded_columns_index = expand_grid(puzzle_input)
    print_grid(puzzle_input)
    print(len(puzzle_input))
    print(len(puzzle_input[0]))

    print('')
    print(expanded_columns_index)
    print(expanded_rows_index)
    print('')

    puzzle_input, gal_num = number_galaxies(puzzle_input)
    alt_puzzle, gal_num = number_galaxies(original_puzzle)
    # print_grid(puzzle_input)

    gal_pairs = generate_pairs(gal_num)
    print(gal_pairs)
    print(len(gal_pairs))
    print('')

    pair_coords = []
    for pair in gal_pairs:
        pc = get_pair_coords(pair, alt_puzzle, expanded_columns_index, expanded_rows_index)
        pair_coords.append(pc)
    print(pair_coords)
    print(len(pair_coords))
    print('')

    distances = []
    for coords in pair_coords:
        distance = calc_distance(coords[0], coords[1])
        distances.append(distance)
    print(distances)
    print(len(distances))
    print('')

    print(sum(distances))


if __name__ == '__main__':
    puzzle_input = read_input('part_2_puzzle_11_example_input.txt')
    # puzzle_input = read_input('part_2_puzzle_11_input.txt')
    main(puzzle_input)
