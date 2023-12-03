""" Part 2 of Puzzle 1 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/1


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            puzzle_input.append(line)
        return puzzle_input


def get_calibration_value(line):
    string_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_in_line = []
    char_stack = []
    sanitized_line = line.strip('\n')
    for char in sanitized_line:
        try:
            # if we hit an integer, put it in the list of numbers and clear the char_stack
            number = int(char)
            numbers_in_line.append(number)
            char_stack = []
        except ValueError:
            # if we hit a char, add it to the stack and check the stack for valid numbers
            char_stack.append(char)
            char_string = ''.join(char_stack)
            for key in string_numbers.keys():
                if key in char_string:
                    # if we find a number in the char_stack, add that number to the number list
                    numbers_in_line.append(string_numbers[key])
                    # reset the char_stack to the number we found minus the first letter to avoid duplicate finds
                    char_string = key
                    char_stack = list(char_string)
                    char_stack.pop(0)
    if len(numbers_in_line) > 1:
        calibration_value = f'{numbers_in_line[0]}{numbers_in_line[-1]}'
    else:
        # if there is only 1 number, return it twice as first and last digit
        calibration_value = f'{numbers_in_line[0]}{numbers_in_line[0]}'
    return int(calibration_value)


def get_calibration_sum(calibration_values):
    return sum(calibration_values)


def main():
    puzzle_input = read_input('part_2_puzzle_1_input.txt')
    calibration_values = []
    for line in puzzle_input:
        calibration_values.append(get_calibration_value(line))
    calibration_sum = get_calibration_sum(calibration_values)
    print(calibration_sum)


if __name__ == '__main__':
    main()
