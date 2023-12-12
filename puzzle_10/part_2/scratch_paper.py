""" Puzzle 2 for Puzzle 10 for Advent of Code 2023 """
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


DIRECTIONS = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}


def convert_to_pipes(tile_map):
    pipe_chart = {
        '|': '║',
        '-': '═',
        'L': '╚',
        'J': '╝',
        '7': '╗',
        'F': '╔',
    }
    converted_map = []
    for row in tile_map:
        for i in range(len(row)):
            if row[i] in pipe_chart.keys():
                row[i] = pipe_chart[row[i]]
        converted_map.append(row)
    return converted_map


def get_next_direction(current_pipe, direction):
    if current_pipe in "║═S":
        return direction
    elif current_pipe == "╚":
        return 'E' if direction == 'S' else ('N' if direction == 'W' else None)
    elif current_pipe == "╝":
        return 'N' if direction == 'E' else ('W' if direction == 'S' else None)
    elif current_pipe == "╗":
        return 'S' if direction == 'E' else ('W' if direction == 'N' else None)
    elif current_pipe == "╔":
        return 'S' if direction == 'W' else ('E' if direction == 'N' else None)

    # Raise ValueError when meeting unknown pipe character.
    raise ValueError("Unknown pipe character: " + current_pipe)


def get_next_position(position, direction):
    deltas = DIRECTIONS[direction]
    return position[0] + deltas[0], position[1] + deltas[1]


def trace_pipes(converted_map, start_dir):
    rows = len(converted_map)
    cols = len(converted_map[0]) if rows else 0

    # find the starting position
    start = None
    for i in range(rows):
        for j in range(cols):
            if converted_map[i][j] == "S":
                start = (i, j)

    if not start:
        return "Start position not found."

    start_direction = start_dir

    position = start
    direction = start_direction  # initially we'll move to the right (could be other way around based on your rules)
    pipes = []

    steps = 0
    pipe_complete = False
    while not pipe_complete:
        direction = get_next_direction(converted_map[position[0]][position[1]], direction)
        pipes.append(position)

        # if we've made it back to the start, we're done
        if steps > 0 and position == start:
            pipe_complete = True

        # if we're about to walk off the grid, or into a ground, we can't complete the loop
        if (
                position[0] not in range(rows) or
                position[1] not in range(cols) or
                converted_map[position[0]][position[1]] == '.'
        ):
            return "Cannot complete the loop."

        position = get_next_position(position, direction)
        steps += 1

    marked_map = find_left_right(converted_map, pipes, start_dir)
    return marked_map


def find_left_right(converted_map, pipes, direction):
    left_tiles = []
    right_tiles = []
    for pipe in pipes:
        direction = get_next_direction(converted_map[pipe[0]][pipe[1]], direction)

        if direction == 'E':
            left_loc = (pipe[0] - 1, pipe[1])
            right_loc = (pipe[0] + 1, pipe[1])

            if left_loc not in pipes:
                left_tiles.append(left_loc)
            if right_loc not in pipes:
                right_tiles.append(right_loc)

        elif direction == 'W':
            left_loc = (pipe[0] + 1, pipe[1])
            right_loc = (pipe[0] - 1, pipe[1])

            if left_loc not in pipes:
                left_tiles.append(left_loc)
            if right_loc not in pipes:
                right_tiles.append(right_loc)

        elif direction == 'N':
            left_loc = (pipe[0], pipe[1] - 1)
            right_loc = (pipe[0], pipe[1] + 1)

            if left_loc not in pipes:
                left_tiles.append(left_loc)
            if right_loc not in pipes:
                right_tiles.append(right_loc)

        elif direction == 'S':
            left_loc = (pipe[0], pipe[1] + 1)
            right_loc = (pipe[0], pipe[1] - 1)

            if left_loc not in pipes:
                left_tiles.append(left_loc)
            if right_loc not in pipes:
                right_tiles.append(right_loc)

    marked_map = mark_left_right(converted_map, left_tiles, right_tiles, pipes)
    return marked_map


def mark_left_right(converted_map, left_tiles, right_tiles, pipes):
    for l in left_tiles:
        if 0 <= l[0] < len(converted_map) and 0 <= l[1] < len(converted_map[0]):
            painted_grid = paint(l, converted_map, 'I')
        else:
            print(
                f'Index {l} is out of bounds for painted_grid with dimensions {len(converted_map)}x{len(converted_map[0])}')
    flood(converted_map, pipes, fill_char='I')

    for r in right_tiles:
        if 0 <= r[0] < len(converted_map) and 0 <= r[1] < len(converted_map[0]):
            painted_grid = paint(r, converted_map, 'O')
        else:
            print(
                f'Index {r} is out of bounds for painted_grid with dimensions {len(converted_map)}x{len(converted_map[0])}')
    flood(converted_map, pipes, fill_char='O')

    for t, row in enumerate(converted_map):
        for i, tile in enumerate(converted_map[t]):
            if converted_map[t][i] == 'O':
                break
            else:
                painted_grid = paint((t, i), converted_map, 'O')

    for t, row in enumerate(converted_map):
        for i, tile in enumerate(converted_map[t]):
            if 0 <= t < len(converted_map) and 0 <= i < len(converted_map[0]) and (t, i) not in pipes:
                if converted_map[t][i] != 'O' and converted_map[t][i] != 'I':
                    painted_grid = paint((t, i), converted_map, 'X')
                else:
                    print(
                        f'Index {t, i} is out of bounds for painted_grid with dimensions {len(converted_map)}x{len(converted_map[0])}')

    # print_maps([painted_grid])
    print('Pipe tracing complete.')
    # print(pipes)
    return painted_grid


def paint(coords, converted_map, paint_char='X'):
    converted_map[coords[0]][coords[1]] = paint_char
    return converted_map


def print_maps(tile_map):
    for row in tile_map:
        print(row)
        
        
def flood(painted_grid, pipes, fill_char='I', spread=True):
    if spread:
        for i, row in enumerate(painted_grid):
            for j, char in enumerate(row):
                if char == fill_char:
                    up = (i - 1, j)
                    down = (i + 1, j)
                    left = (i, j - 1)
                    right = (i, j + 1)
                    dirs = [up, down, left, right]
                    for d in dirs:
                        if len(painted_grid) > d[0] and len(painted_grid[d[0]]) > d[1]:
                            # if painted_grid[d[0]][d[1]] != barrier:
                            if d not in pipes:
                                paint((d[0], d[1]), painted_grid, fill_char)

        for i, row in reversed(list(enumerate(painted_grid))):
            for j, char in reversed(list(enumerate(row))):
                if char == 'I':
                    up = (i - 1, j)
                    down = (i + 1, j)
                    left = (i, j - 1)
                    right = (i, j + 1)
                    dirs = [up, down, left, right]
                    for d in dirs:
                        if len(painted_grid) > d[0] and len(painted_grid[d[0]]) > d[1]:
                            # if painted_grid[d[0]][d[1]] != barrier:
                            if d not in pipes:
                                paint((d[0], d[1]), painted_grid, 'I')

    print_maps([painted_grid])


def main(puzzle_input):
    tile_map = []
    for line in puzzle_input:
        tile_map.append(list(line))

    converted_map = convert_to_pipes(tile_map)
    print_maps(converted_map)

    marked_grid = trace_pipes(converted_map, 'W')

    print_maps(marked_grid)

    for line in marked_grid:
        print(''.join(line))

    inner_count = 0
    for line in marked_grid:
        inner_count += line.count('I')

    print(inner_count)


if __name__ == '__main__':
    puzzles = []
    # puzzles.append(read_input('part_2_puzzle_10_example_input.txt'))
    # puzzles.append(read_input('part_2_puzzle_10_alt_example_2_input.txt'))
    # puzzles.append(read_input('part_2_puzzle_10_alt_example_3_input.txt'))
    # puzzles.append(read_input('part_2_puzzle_10_alt_example_input.txt'))

    puzzles.append(read_input('part_2_puzzle_10_input.txt'))

    for p in puzzles:
        main(p)
