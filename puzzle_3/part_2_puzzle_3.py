""" Part 2 for Puzzle 3 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/3


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            puzzle_input.append(line[:-1])
        return puzzle_input


def get_gears_indices(puzzle_input):
    gears_indices = {}
    for line_index, line in enumerate(puzzle_input):
        gears_indices[line_index] = []
        gears_stack = []
        for i, char in enumerate(line):
            if char == '*':
                gears_stack.append(i)
                if i == len(line) - 1:
                    gears_indices[line_index].append(gears_stack)
                    gears_stack = []
            else:
                if len(gears_stack) > 0:
                    gears_indices[line_index].append(gears_stack)
                    gears_stack = []
    return gears_indices


def check_indices_on_other_line(indices, line):
    target_indices = []
    for i, index in enumerate(indices):
        # if the number is not at the start of the line, check 1 to the left
        if i == 0 and index != 0:
            try:
                int(line[indices[0] - 1])
                target_index = indices[0] - 1
                # if a number is found keep checking left until you get the whole number
                while target_index >= 0:
                    try:
                        int(line[target_index])
                        target_indices.insert(0, line[target_index])
                        target_index -= 1
                    except ValueError:
                        break
            except ValueError:
                pass
        # check the line at the spots directly above/below the numbers
        target_indices.append(line[index])
        # if the number is not at the end of the line, check 1 to the right
        if i == len(indices) - 1 and index != len(line) - 1:
            try:
                int(line[indices[-1] + 1])
                target_index = indices[-1] + 1
                while target_index <= len(line) - 1:
                    try:
                        int(line[target_index])
                        target_indices.append(line[target_index])
                        target_index += 1
                    except ValueError:
                        break
            except ValueError:
                pass
    return target_indices


def check_indices_on_same_line(indices, line):
    adjacent_indices = []
    if indices[0] != 0:
        try:
            int(line[indices[0] - 1])
            target_index = indices[0] - 1
            while target_index >= 0:
                try:
                    int(line[target_index])
                    adjacent_indices.insert(0, line[target_index])
                    target_index -= 1
                except ValueError:
                    break
        except ValueError:
            pass
    adjacent_indices.append('.')  # account for numbers on either side of the gear
    if indices[-1] != len(line) - 1:
        try:
            int(line[indices[-1] + 1])
            target_index = indices[-1] + 1
            while target_index <= len(line) - 1:
                try:
                    int(line[target_index])
                    adjacent_indices.append(line[target_index])
                    target_index += 1
                except ValueError:
                    break
        except ValueError:
            pass
    return adjacent_indices


def check_gear_validity(target_indices):
    joined_indices = []
    for index in target_indices:
        joined_index = ''.join(index)
        numbers_in_index = joined_index.split('.')
        joined_indices.append(numbers_in_index)

    adjacent_part_numbers = 0
    adjacent_part_number_values = []
    for index in joined_indices:
        for part_number in index:
            try:
                int(part_number)
                adjacent_part_numbers += 1
                adjacent_part_number_values.append(int(part_number))
            except ValueError:
                pass
    if adjacent_part_numbers == 2:
        gear_ratio = 1
        for part_number in adjacent_part_number_values:
            gear_ratio *= part_number
        return True, gear_ratio
    return False, []


def find_gears(gears_indices, puzzle_input):
    gear_ratios = []
    for line_with_number in gears_indices:
        for i, potential_gear in enumerate(gears_indices[line_with_number]):
            target_indices = []
            # check the same indices on above
            # check the index before and after the number on the same line
            # check the same indices on the line below
            if line_with_number == 0:
                target_indices.append(check_indices_on_same_line(potential_gear, puzzle_input[line_with_number]))
                target_indices.append(check_indices_on_other_line(potential_gear, puzzle_input[line_with_number + 1]))
            elif line_with_number == len(puzzle_input) - 1:
                target_indices.append(check_indices_on_other_line(potential_gear, puzzle_input[line_with_number - 1]))
                target_indices.append(check_indices_on_same_line(potential_gear, puzzle_input[line_with_number]))
            else:
                target_indices.append(check_indices_on_other_line(potential_gear, puzzle_input[line_with_number - 1]))
                target_indices.append(check_indices_on_same_line(potential_gear, puzzle_input[line_with_number]))
                target_indices.append(check_indices_on_other_line(potential_gear, puzzle_input[line_with_number + 1]))

            # if there was anything other than a . that was not an int then the number is a part number
            is_gear, gear_ratio = check_gear_validity(target_indices)
            if is_gear:
                gear_ratios.append(gear_ratio)
    return gear_ratios


def main():
    # read each line and get the indices of the numbers
    puzzle_input = read_input('part_2_puzzle_3_input.txt')
    gears_indices = get_gears_indices(puzzle_input)

    # find valid gear ratios and print the sum of the numbers
    gear_ratios = find_gears(gears_indices, puzzle_input)
    print(sum(gear_ratios))


if __name__ == '__main__':
    main()
