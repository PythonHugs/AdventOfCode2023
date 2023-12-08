""" Puzzle 8 for Advent of Code 2023 """
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


def parse_data(puzzle_input):
    map = {}
    directions = None
    for i, line in enumerate(puzzle_input):
        if i == 0:
            directions = line
            continue
        if line == '':
            continue
        k, v = line.split(' = ')
        options = v
        o1, o2 = options.split(',')
        map[k] = tuple((o1[1:], o2[1:-1]))
    return directions, map


def traverse_map(elf_map, directions):
    starting_point = 'AAA'
    current_position = starting_point
    steps = 0

    while current_position != 'ZZZ':
        for d in directions:
            if d == 'R':
                destination = elf_map[current_position][1]
                current_position = destination
            else:
                destination = elf_map[current_position][0]
                current_position = destination
            steps += 1
            print(f'Step {steps}: Moving from {current_position} to {destination}')
    return steps


def main():
    puzzle_input = read_input('puzzle_8_input.txt')
    print(puzzle_input)
    print('')

    directions, elf_map = parse_data(puzzle_input)

    print(f'Directions: {directions}')
    print('')
    print('Elf Map:')
    for data in elf_map:
        print(f'{data}: {elf_map[data][0]} {elf_map[data][1]}')
    print('')

    total_steps = traverse_map(elf_map, directions)
    print('')
    print(f'Total steps: {total_steps}')


if __name__ == '__main__':
    main()
