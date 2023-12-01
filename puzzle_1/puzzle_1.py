""" Puzzle 1 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/1


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            puzzle_input.append(line)
        return puzzle_input


def get_calibration_value(line):
    numbers_in_line = []
    for char in line:
        try:
            number = int(char)
            numbers_in_line.append(number)
        except ValueError:
            continue
    calibration_value = f'{numbers_in_line[0]}{numbers_in_line[-1]}'
    return int(calibration_value)


def get_calibration_sum(calibration_values):
    return sum(calibration_values)


def main():
    puzzle_input = read_input('puzzle_1_input.txt')
    calibration_values = []
    for line in puzzle_input:
        calibration_values.append(get_calibration_value(line))
    calibration_sum = get_calibration_sum(calibration_values)
    print(calibration_sum)


if __name__ == '__main__':
    main()
