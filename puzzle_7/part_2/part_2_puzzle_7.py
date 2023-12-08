""" Part 2 for Puzzle 7 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/7


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
    hands = []
    bids = []
    for data in puzzle_input:
        hand, bid = data.split(' ')
        hands.append(hand)
        bids.append(int(bid))
    hands_data = {}
    for i in range(len(hands)):
        hands_data[i] = {}
        hands_data[i]['cards'] = hands[i]
        hands_data[i]['bid'] = bids[i]
        hands_data[i]['type'] = count_hand(hands[i])
    return hands_data


def count_hand(hand):
    card_key = {
        'A': 0,
        'K': 0,
        'Q': 0,
        'J': 0,
        'T': 0,
        '9': 0,
        '8': 0,
        '7': 0,
        '6': 0,
        '5': 0,
        '4': 0,
        '3': 0,
        '2': 0,
    }
    for card in hand:
        card_key[card] += 1
    hand_type = ''

    max_card = max(card_key, key=card_key.get)
    print(hand)
    print(f'max card is {max_card} x {card_key[max_card]}')
    if max_card != 'J':
        card_key[max_card] += card_key['J']
        card_key['J'] = 0
    elif max_card == 'J':
        temp_j_holder = card_key['J']
        card_key['J'] = 0
        max_card = max(card_key, key=card_key.get)
        card_key[max_card] += temp_j_holder
    print('-----')
    print(hand.replace('J', max_card))
    print(f'max card is {max_card} x {card_key[max_card]}')
    print('')

    if 5 in card_key.values():
        hand_type = 'five of a kind'
    elif 4 in card_key.values():
        hand_type = 'four of a kind'
    elif 3 in card_key.values():
        if 2 in card_key.values():
            hand_type = 'full house'
        else:
            hand_type = 'three of a kind'
    elif 2 in card_key.values():
        num_pairs = 0
        for value in card_key.values():
            if value == 2:
                num_pairs += 1
            if num_pairs == 2:
                hand_type = 'two pairs'
            else:
                hand_type = 'one pair'
    else:
        hand_type = 'high card'
    return hand_type


def output_hands_data(hands_data):
    for hands in hands_data.items():
        print(hands)
    print('')


def categorize_hands(hand_types, hands_data):
    hand_types_dict = {hand_type: [] for hand_type in hand_types}
    for hand_type in hand_types:
        for hand in hands_data:
            if hands_data[hand]['type'] == hand_type:
                hand_types_dict[hand_type].append(hands_data[hand])
    return hand_types_dict


def translate_cards(categorized_hands):
    for hand_type, hands in categorized_hands.items():
        translated_cards = []
        for hand in hands:
            for card in hand['cards']:
                if card == 'A':
                    translated_cards.append(14)
                elif card == 'K':
                    translated_cards.append(13)
                elif card == 'Q':
                    translated_cards.append(12)
                elif card == 'J':
                    translated_cards.append(1)
                elif card == 'T':
                    translated_cards.append(10)
                else:
                    translated_cards.append(int(card))
            categorized_hands[hand_type][categorized_hands[hand_type].index(hand)]['cards'] = translated_cards
            translated_cards = []


def translate_hands(categorized_hands):
    translated_hands = []
    for hand_data in categorized_hands.items():
        sorted_hand_data = sorted(hand_data[1], key=lambda x: x['cards'], reverse=True)
        print(sorted_hand_data)
        if sorted_hand_data:
            translated_hands.append(sorted_hand_data)
    print('')
    for data in translated_hands:
        print(data)
    print('')
    return translated_hands


def determine_winnings(translated_hands):
    ranked_bids = []
    for hand_type in translated_hands:
        for hand in reversed(hand_type):
            print(hand)
            ranked_bids.append(hand['bid'])
    print('')
    winnings = []
    for bid in ranked_bids:
        bid_index = ranked_bids.index(bid)
        earned = bid * (ranked_bids.index(bid) + 1)
        print(bid, bid_index, earned)
        winnings.append(earned)
    print('')
    return sum(winnings)


def main():
    puzzle_input = read_input('part_2_puzzle_7_input.txt')
    print(puzzle_input)
    print('')

    hands_data = parse_data(puzzle_input)
    output_hands_data(hands_data)

    # split hands into types
    hand_types = [
        'high card',
        'one pair',
        'two pairs',
        'three of a kind',
        'full house',
        'four of a kind',
        'five of a kind'
    ]

    categorized_hands = categorize_hands(hand_types, hands_data)
    output_hands_data(categorized_hands)

    translate_cards(categorized_hands)
    output_hands_data(categorized_hands)

    translated_hands = translate_hands(categorized_hands)

    total_winnings = determine_winnings(translated_hands)
    print(total_winnings)


if __name__ == '__main__':
    main()
