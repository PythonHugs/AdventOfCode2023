""" Puzzle 4 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/4


def read_input(input_file):
    with open(input_file, 'r') as file:
        puzzle_input = []
        for line in file:
            puzzle_input.append(line[:-1])
        return puzzle_input


def parse_numbers(nums):
    numbers = []
    for n in nums.split(' '):
        try:
            int(n)
            numbers.append(n)
        except ValueError:
            continue
    return numbers


def parse_cards(puzzle_input):
    card_data = {}
    for i, line in enumerate(puzzle_input):
        nums_in_line = line.split(':')[1].split('|')
        winning_nums = parse_numbers(nums_in_line[0])
        my_nums = parse_numbers(nums_in_line[1])
        card_data[i] = [winning_nums, my_nums]
    return card_data


def find_matches(winning_nums, my_nums):
    num_matches = 0
    for num in my_nums:
        if num in winning_nums:
            num_matches += 1
    return num_matches


def calculate_points(num_matches):
    points = 0
    if num_matches == 0:
        return points
    if num_matches >= 1:
        points += 1
    for match in range(num_matches - 1):
        points = points + points
    return points


def main():
    puzzle_input = read_input('puzzle_4_input.txt')
    card_data = parse_cards(puzzle_input)
    cards_value = 0
    for card in card_data:
        winning_nums = card_data[card][0]
        my_nums = card_data[card][1]
        num_matches = find_matches(winning_nums, my_nums)
        card_points = calculate_points(num_matches)
        cards_value += card_points
    print(cards_value)


if __name__ == '__main__':
    main()
