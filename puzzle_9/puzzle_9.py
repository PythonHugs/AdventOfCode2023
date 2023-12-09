""" Puzzle 9 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/9


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            if '\n' in line:
                puzzle_input.append(line[:-1])
            else:
                puzzle_input.append(line)
        return puzzle_input


def count_skips(converted_list):
    last_values = []
    next_list = []
    for i in range(len(converted_list) - 1):
        next_list.append(converted_list[i + 1] - converted_list[i])
        if i == len(converted_list) - 2:
            last_values.append(next_list[i])
    return last_values, next_list


def run_counter(converted_list):
    last_skips = []
    while not all(value == 0 for value in converted_list):
        lv, next_list = count_skips(converted_list)
        last_skips.extend(lv)
        converted_list = next_list
    return last_skips, converted_list


def get_history(puzzle_input):
    history = []
    for data in puzzle_input:
        test = data.split(' ')
        converted_list = list(map(int, test))

        print(converted_list)

        last_skips, last_list = run_counter(converted_list)
        last_skips.reverse()
        # print(last_list)
        print(last_skips)

        next_value = [0]
        for i in range(len(last_skips)):
            next_value.append(last_skips[i] + next_value[-1])
        next_value.append(converted_list[-1] + next_value[-1])
        print(next_value)
        history.append(next_value[-1])
    return history


def main():
    # puzzle_input = read_input('puzzle_9_example_input.txt')
    puzzle_input = read_input('puzzle_9_input.txt')
    print(puzzle_input)
    print('')

    history = get_history(puzzle_input)
    print(sum(history))


if __name__ == '__main__':
    main()
