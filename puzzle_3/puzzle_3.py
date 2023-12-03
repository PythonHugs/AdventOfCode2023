""" Puzzle 3 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/3


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            puzzle_input.append(line[:-1])
        return puzzle_input


def get_part_numbers(puzzle_input):
    part_number_indices = {}
    for line_index, line in enumerate(puzzle_input):
        part_number_indices[line_index] = []
        int_stack = []
        for i, char in enumerate(line):
            try:
                int(char)
                int_stack.append(char)
                if i == len(line) - 1:
                    part_number_indices[line_index].append(int(''.join(int_stack)))
                    int_stack = []
            except ValueError:
                if len(int_stack) > 0:
                    part_number_indices[line_index].append(int(''.join(int_stack)))
                    int_stack = []
    return part_number_indices


def get_part_number_indices(puzzle_input):
    part_number_indices = {}
    for line_index, line in enumerate(puzzle_input):
        part_number_indices[line_index] = []
        int_stack = []
        for i, char in enumerate(line):
            try:
                int(char)
                int_stack.append(i)
                if i == len(line) - 1:
                    part_number_indices[line_index].append(int_stack)
                    int_stack = []
            except ValueError:
                if len(int_stack) > 0:
                    part_number_indices[line_index].append(int_stack)
                    int_stack = []
    return part_number_indices


def check_indices_on_other_line(indices, line):
    target_indices = []
    for i, index in enumerate(indices):
        # if the number is not at the start of the line, check 1 to the left
        if i == 0 and index != 0:
            target_indices.insert(0, line[indices[0] - 1])
        # check the line at the stops directly above/below the numbers
        target_indices.append(line[index])
        # if the number is not at the end of the line, check 1 to the right
        if i == len(indices) - 1 and index != len(line) - 1:
            target_indices.append(line[indices[-1] + 1])
    return target_indices


def check_indices_on_same_line(indices, line):
    adjacent_indices = []
    if indices[0] != 0:
        adjacent_indices.append(line[indices[0] - 1])
    if indices[-1] != len(line) - 1:
        adjacent_indices.append(line[indices[-1] + 1])
    return adjacent_indices


def check_for_part_number(target_indices):
    is_part_number = False
    for places_to_check in target_indices:
        for place in places_to_check:
            if place != '.' and not isinstance(place, int):
                is_part_number = True
    return is_part_number


def find_part_numbers(part_number_indices, part_numbers, puzzle_input):
    valid_part_numbers = []
    for line_with_number in part_number_indices:
        for i, potential_part_number in enumerate(part_number_indices[line_with_number]):
            target_indices = []
            # check the same indices on above
            # check the index before and after the number on the same line
            # check the same indices on the line below
            if line_with_number == 0:
                target_indices.append(check_indices_on_same_line(potential_part_number, puzzle_input[line_with_number]))
                target_indices.append(check_indices_on_other_line(potential_part_number, puzzle_input[line_with_number + 1]))
            elif line_with_number == len(puzzle_input) - 1:
                target_indices.append(check_indices_on_other_line(potential_part_number, puzzle_input[line_with_number - 1]))
                target_indices.append(check_indices_on_same_line(potential_part_number, puzzle_input[line_with_number]))
            else:
                target_indices.append(check_indices_on_other_line(potential_part_number, puzzle_input[line_with_number - 1]))
                target_indices.append(check_indices_on_same_line(potential_part_number, puzzle_input[line_with_number]))
                target_indices.append(check_indices_on_other_line(potential_part_number, puzzle_input[line_with_number + 1]))

            # if there was anything other than a . that was not an int then the number is a part number
            is_part_number = check_for_part_number(target_indices)
            if is_part_number:
                valid_part_numbers.append(part_numbers[line_with_number][i])
    return valid_part_numbers


def main():
    # read each line and get the indices of the numbers
    puzzle_input = read_input('puzzle_3_input.txt')
    part_number_indices = get_part_number_indices(puzzle_input)
    part_numbers = get_part_numbers(puzzle_input)

    # find valid part numbers and print the sum of the numbers
    valid_part_numbers = find_part_numbers(part_number_indices, part_numbers, puzzle_input)
    print(sum(valid_part_numbers))


if __name__ == '__main__':
    main()
