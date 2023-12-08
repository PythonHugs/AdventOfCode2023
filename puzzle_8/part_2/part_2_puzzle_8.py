""" Part 2 for Puzzle 8 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/8
import math


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
    current_positions = []
    steps = 0

    nodes = list(elf_map.keys())
    for node in nodes:
        if node[-1] == 'A':
            current_positions.append(node)

    destinations = []
    for options in elf_map.values():
        destinations.append(str(options[0]) + str(options[1]))

    print(current_positions)
    print(nodes)
    print(destinations)
    print('')

    test_steps = []
    for i in range(len(current_positions)):
        current_position = current_positions[i]
        print(f'Altered current_possitions: {current_positions}')

        while current_position[-1] != 'Z':
            for d in directions:
                if d == 'R':
                    current_destinations = destinations[nodes.index(current_position)][3:]
                else:
                    current_destinations = destinations[nodes.index(current_position)][:3]
                print(f'Step {steps}: Moving from {current_position} to {current_destinations}')
                current_position = current_destinations
                steps += 1
        print(f'Final Destination: {current_destinations}')
        test_steps.append(steps)
        steps = 0
    print(test_steps)

    lcm_value = test_steps[0]
    for i in test_steps[1:]:
        lcm_value = math.lcm(lcm_value, i)

    print(lcm_value)


def main():
    puzzle_input = read_input('part_2_puzzle_8_input.txt')
    print(puzzle_input)
    print('')

    directions, elf_map = parse_data(puzzle_input)

    print(f'Directions: {directions}')
    print('')
    print('Elf Map:')
    for data in elf_map:
        print(f'{data}: {elf_map[data][0]} {elf_map[data][1]}')
    print('')

    traverse_map(elf_map, directions)


if __name__ == '__main__':
    main()
