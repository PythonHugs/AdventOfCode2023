""" Puzzle 2 for Puzzle 8 Advent of Code 2023 """
# https://adventofcode.com/2023/day/8


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def main():
    puzzle_input = read_input('part_2_puzzle_8_example_input.txt')
    print(puzzle_input)
    print('')


if __name__ == '__main__':
    main()
