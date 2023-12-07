""" Puzzle 7 for Advent of Code 2023 """
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
    return hands, bids


def count_hand(hand):
    key = {
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
        key[card] += 1

    hand_type = ''

    if 5 in key.values():
        hand_type = 'five of a kind'
    elif 4 in key.values():
        hand_type = 'four of a kind'
    elif 3 in key.values():
        if 2 in key.values():
            hand_type = 'full house'
        else:
            hand_type = 'three of a kind'
    elif 2 in key.values():
        num_pairs = 0
        for value in key.values():
            if value == 2:
                num_pairs += 1
            if num_pairs == 2:
                hand_type = 'two pairs'
            else:
                hand_type = 'one pair'
    else:
        hand_type = 'high card'

    return hand_type


def rank_hands(hands_data_list):
    hierarchy = [
        'high card',
        'one pair',
        'two pairs',
        'three of a kind',
        'full house',
        'four of a kind',
        'five of a kind'
    ]
    for i in range(len(hands_data_list)):
        hands_data_list[i]['rank'] = hierarchy.index(hands_data_list[i]['type'])
    sorted_hands_data = sorted(hands_data_list, key=lambda h: h['rank'])
    return sorted_hands_data


def sort_ranked_hands(hands_data):
    ranks = []
    hands = []
    for i in range(len(hands_data.keys())):
        ranks.append([hands_data[i]['rank'], i])
        hands.append(hands_data[i]['cards'])
    print(ranks)
    print(hands)
    print('')

    rank_sorted_hands = sorted(ranks)
    return rank_sorted_hands


def break_ties(hands_data_list):
    challenge = []
    card_value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    hierarchy = [
        'high card',
        'one pair',
        'two pairs',
        'three of a kind',
        'full house',
        'four of a kind',
        'five of a kind'
    ]
    for i in range(len(hands_data_list) - 1):
        challenge = []
        try:
            hand_1 = hands_data_list[i]
            hand_2 = hands_data_list[i + 1]
            # if hand_1['type'] != hand_2['type']:
            #     if hierarchy.index(hand_1['type']) > hierarchy.index(hand_2['type']) and hand_1['rank'] == hand_2['rank']:
            #         if hand_1['rank'] != len(hands_data_list) - 1:
            #             hand_1['rank'] += 2
            #             break
            #     elif hierarchy.index(hand_1['type']) < hierarchy.index(hand_2['type']) and hand_1['rank'] == hand_2['rank']:
            #         if hand_2['rank'] != len(hands_data_list) - 1:
            #             hand_2['rank'] += 2
            #             break
            temp_hold = []
            if hand_1['type'] == hand_2['type']:
                for x in range(len(hand_1['cards'])):
                    hand_1_card_value = card_value.index(hand_1['cards'][x])
                    hand_2_card_value = card_value.index(hand_2['cards'][x])
                    if hand_1_card_value == hand_2_card_value:
                        continue
                    if hand_1_card_value > hand_2_card_value:
                        temp_hold.append(hand_1)
                        hand_1 = hand_2
                        hand_2 = temp_hold[0]

            #         elif hand_1_card_value < hand_2_card_value:
            #             if hand_2['rank'] != len(hands_data_list) - 1:
            #                 hand_2['rank'] += 1
            #                 break
            # elif hand_1['type'] == hand_2['type']:
            #     for x in range(len(hand_1['cards'])):
            #         hand_1_card_value = card_value.index(hand_1['cards'][x])
            #         hand_2_card_value = card_value.index(hand_2['cards'][x])
            #         if hand_1_card_value == hand_2_card_value:
            #             continue
            #         if hand_1_card_value > hand_2_card_value and hand_1['rank'] < hand_2['rank']:
            #             hand_1['rank'], hand_2['rank'] = hand_2['rank'], hand_1['rank']
            #             break
            #         elif hand_1_card_value < hand_2_card_value and hand_1['rank'] > hand_2['rank']:
            #             hand_1['rank'], hand_2['rank'] = hand_2['rank'], hand_1['rank']
            #             break

        except IndexError:
            pass

        print(challenge)

    # check_list = []
    # for i in range(len(hands_data_list)):
    #     check_list.append(hands_data_list[i]['rank'])

    # print(check_list)
    # print(set(check_list))

    # sorted_hands_data = sorted(hands_data_list, key=lambda h: h['rank'])
    # if i == len(hands_data_list) - 1:
    #     return break_ties(sorted_hands_data)
    return hands_data_list


def output_hand_data(hands_data_list):
    for i in range(len(hands_data_list)):
        print(hands_data_list[i])
    print('')


def main():
    puzzle_input = read_input('puzzle_7_example_input.txt')
    print(puzzle_input)
    print('')

    hands, bids = parse_data(puzzle_input)
    # print(hands)
    # print(bids)
    # print('')

    hands_data = {}
    for i in range(len(hands)):
        hands_data[i] = {}
        hands_data[i]['cards'] = hands[i]
        hands_data[i]['bid'] = bids[i]
        hands_data[i]['type'] = count_hand(hands[i])

    hands_data_list = []
    for hand in hands_data.keys():
        hands_data_list.append(hands_data[hand])

    sorted_hands_data = rank_hands(hands_data_list)
    output_hand_data(sorted_hands_data)

    final_hands_data = break_ties(sorted_hands_data)
    output_hand_data(final_hands_data)

    # rank_sorted_hands = sort_ranked_hands(hands_data)
    # print(rank_sorted_hands)
    # print('')
    #
    # ranked_hands = break_ties(rank_sorted_hands, hands)
    # print(ranked_hands)
    # print('')

    # for i in range(len(ranked_hands) - 1, -1, -1):
    #     print(hands[i])




if __name__ == '__main__':
    main()
