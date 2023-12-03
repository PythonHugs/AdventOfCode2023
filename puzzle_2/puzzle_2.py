""" Puzzle 2 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/2


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def get_games_from_puzzle_input(puzzle_input):
    cube_reveals = []
    for game in puzzle_input:
        raw_reveals = game.split(':')[1].split(';')
        sanitized_reveals = []
        for reveal in raw_reveals:
            sanitized_reveals.append(reveal.replace(' ', ''))
        cube_reveals.append(sanitized_reveals)
    return cube_reveals


def split_cubes(cube_reveal):
    return cube_reveal.split(',')


def get_cube_number(cubes):
    num_cubes = []
    for char in cubes:
        try:
            int(char)
            num_cubes.append(char)
        except ValueError:
            continue
    return int(''.join(num_cubes))


def get_cube_color(cubes):
    color = []
    for char in cubes:
        try:
            int(char)
        except ValueError:
            color.append(char)
    return ''.join(color)


def is_game_possible(cube_color, cube_number):
    total_cubes = {'red': 12, 'green': 13, 'blue': 14}
    if cube_number > total_cubes[cube_color]:
        return False
    return True


def main():
    # read the puzzle input and get list of game data
    puzzle_input = read_input('puzzle_2_input.txt')
    games_data = get_games_from_puzzle_input(puzzle_input)

    possible_games = 0
    for i, game in enumerate(games_data):
        possible = []
        for cube_reveal in game:
            for cubes in split_cubes(cube_reveal):
                # read the cube data for each reveal to get color and number
                cube_color = get_cube_color(cubes)
                cube_number = get_cube_number(cubes)

                # compare to total cubes to see if game is possible
                possible.append(is_game_possible(cube_color, cube_number))
        if False not in possible:
            possible_games += (i + 1)
    print(possible_games)


if __name__ == '__main__':
    main()
