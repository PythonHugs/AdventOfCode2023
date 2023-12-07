""" Puzzle 2 for Puzzle 6 Advent of Code 2023 """
# https://adventofcode.com/2023/day/6


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
    times = puzzle_input[0].split(':')[1].split(' ')
    distances = puzzle_input[1].split(':')[1].split(' ')
    cleaned_times, cleaned_distances = clean_data(times, distances)
    return int(''.join(cleaned_times)), int(''.join(cleaned_distances))


def clean_data(times, distances):
    cleaned_times = []
    cleaned_distances = []
    for time in times:
        try:
            int(time)
            cleaned_times.append(time)
        except ValueError:
            continue
    for distance in distances:
        try:
            int(distance)
            cleaned_distances.append(distance)
        except ValueError:
            continue
    return cleaned_times, cleaned_distances


def find_winning_button_press_length(time, distance):
    options = []
    for x in range(1, time + 1):
        if x * (time - x) > distance:
            options.append(x)
            break
    for x in range(time + 1, 1, -1):
        if x * (time - x) > distance:
            options.append(x)
            break
    return options


def main():
    puzzle_input = read_input('part_2_puzzle_6_input.txt')
    print(puzzle_input)

    time, distance = parse_data(puzzle_input)
    print(time)
    print(distance)
    print('')

    button_options = find_winning_button_press_length(time, distance)
    print(button_options)

    final_answer = button_options[1] - button_options[0] + 1
    print(final_answer)


if __name__ == '__main__':
    main()
