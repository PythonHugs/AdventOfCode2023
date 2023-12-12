""" Puzzle 12 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/12


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def main(puzzle_input):
    print(puzzle_input)
    print('')


if __name__ == '__main__':
    puzzle_input = read_input('puzzle_12_example_input.txt')
    # puzzle_input = read_input('puzzle_12_input.txt')
    main(puzzle_input)
