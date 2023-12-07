""" Part 2 for Puzzle 4 for Advent of Code 2023 """
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
    card_data = []
    for i, line in enumerate(puzzle_input):
        nums_in_line = line.split(':')[1].split('|')
        winning_nums = parse_numbers(nums_in_line[0])
        my_nums = parse_numbers(nums_in_line[1])
        card_data.append([winning_nums, my_nums])
    return card_data


def find_matches(winning_nums, my_nums):
    num_matches = 0
    for num in my_nums:
        if num in winning_nums:
            num_matches += 1
    return num_matches


def setup_card_stacks(card_data):
    stacks = []
    initial_stack = []
    for x in range(len(card_data)):
        initial_stack.append(x)
    stacks.append(initial_stack)
    return stacks


def check_stacks(stacks, card_data):
    for card_stack in stacks:
        for card in card_stack:
            winning_nums = card_data[card][0]
            my_nums = card_data[card][1]
            num_matches = find_matches(winning_nums, my_nums)

            cards_copied = []
            copied_data = []
            for x in range(1, num_matches + 1):
                if card + x <= len(card_data) - 1:
                    cards_copied.append(card + x)
                    copied_data.append(card_data[card + x])
            if len(cards_copied) > 0:
                stacks.append(cards_copied)


def count_cards(stacks):
    total_cards = 0
    for card_stack in stacks:
        total_cards += len(card_stack)
    return total_cards


def main():
    puzzle_input = read_input('part_2_puzzle_4_input.txt')
    card_data = parse_cards(puzzle_input)
    print('It works.\nWait for it...')
    stacks = setup_card_stacks(card_data)
    check_stacks(stacks, card_data)
    print(count_cards(stacks))


if __name__ == '__main__':
    main()
