""" Puzzle 10 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/10


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def process_puzzle(puzzle_input):
    processed_puzzle_input = []
    for line in puzzle_input:
        processed_puzzle_input.append(list(line.lower()))
    return processed_puzzle_input


def find_start(processed_puzzle_input):
    for i, line in enumerate(processed_puzzle_input):
        if 's' in line:
            return i, line.index('s')


def get_options(x, y):
    up = [x - 1, y]
    down = [x + 1, y]
    left = [x, y - 1]
    right = [x, y + 1]
    return {'up': up, 'down': down, 'left': left, 'right': right}


def check_tiles(options, tile_map, x, y=None):
    valid_options = []
    for direction in options.keys():
        d = options[direction]
        if d[1] < 0 or d[1] >= len(tile_map[x]) or d[0] < 0 or d[0] >= len(tile_map):
            continue
        if tile_map[d[0]][d[1]] == '.':
            continue
        valid_options.append([direction, d[0], d[1]])
    return valid_options


def output_valid_options(valid_options, tile_map):
    print('Valid options:')
    for vo in valid_options:
        print(f'({vo[0]}) {tile_map[vo[1]][vo[2]]}')


def traverse_map(start_point, tile_map):
    valid_directions = {
        '|': ['up', 'down'],
        '-': ['left', 'right'],
        'l': ['right', 'up'],
        'j': ['left', 'up'],
        '7': ['left', 'down'],
        'f': ['right', 'down']
    }

    opposite_directions = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left'
    }

    x, y = start_point
    options = get_options(x, y)
    valid_options = check_tiles(options, tile_map, x, y)
    default_direction = valid_options[0]
    # print(default_direction)
    x, y = default_direction[1], default_direction[2]
    tile = tile_map[x][y]
    print(f'Moving {default_direction[0]} to: {tile}')
    current_location = default_direction

    pipes_mapped = False
    pipe_steps = 1
    while not pipes_mapped:
        print(f'Currently on: {tile} {x, y}')
        backward = opposite_directions[current_location[0]]
        if tile_map[x][y] != 's':
            options = get_options(x, y)
            valid_options = check_tiles(options, tile_map, x, y)
            for op in valid_options:
                if op[0] in valid_directions[tile] and op[0] != backward:
                    default_direction = op
                    break
            # print(default_direction)
            # print(f'Backward: {backward}')
            x, y = default_direction[1], default_direction[2]
            tile = tile_map[x][y]
            print(f'Moving {default_direction[0]} to: {tile}')
            current_location = default_direction
            pipe_steps += 1
            valid_options = check_tiles(options, tile_map, x, y)
            # output_valid_options(valid_options, tile_map)
        else:
            pipes_mapped = True
    return pipe_steps


def main():
    # puzzle_input = read_input('puzzle_10_example_input.txt')
    puzzle_input = read_input('puzzle_10_input.txt')
    print(puzzle_input)
    print('')

    tile_map = process_puzzle(puzzle_input)
    for line in tile_map:
        print(line)

    print('')

    start_point = list(find_start(tile_map))
    print(f'Starting at: S {start_point}')

    pipe_steps = traverse_map(start_point, tile_map)

    print(f'\n{pipe_steps}')
    print(int(pipe_steps / 2))


if __name__ == '__main__':
    main()
