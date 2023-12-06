""" Puzzle 6 for Advent of Code 2023 """
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
    return clean_data(times, distances)


def clean_data(times, distances):
    cleaned_times = []
    cleaned_distances = []
    for time in times:
        try:
            cleaned_time = int(time)
            cleaned_times.append(cleaned_time)
        except ValueError:
            continue
    for distance in distances:
        try:
            cleaned_distance = int(distance)
            cleaned_distances.append(cleaned_distance)
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


def get_num_ways_to_win_multiplied(num_ways):
    total = 1
    for i in num_ways:
        total = total * i
    return total


def main():
    puzzle_input = read_input('puzzle_6_input.txt')
    print(puzzle_input)

    times, distances = parse_data(puzzle_input)
    print(times)
    print(distances)
    print('')

    num_ways_to_win = []
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        button_options = find_winning_button_press_length(time, distance)
        num_ways_to_win.append(button_options[1] - button_options[0] + 1)

    final_answer = get_num_ways_to_win_multiplied(num_ways_to_win)
    print(final_answer)


if __name__ == '__main__':
    main()
