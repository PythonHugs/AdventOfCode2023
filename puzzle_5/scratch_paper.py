""" Part 2 for Puzzle 5 for Advent of Code 2023 """
import copy
# https://adventofcode.com/2023/day/5
import json


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
    seed_data = {}
    current_category = ''
    for line in puzzle_input:
        if line == '':
            pass
        elif ':' in line:
            current_category = line.split(':')[0]
            if current_category == 'seeds':
                seed_data[current_category] = [int(seed) for seed in line.split(':')[1].split(' ')[1:]]
            else:
                seed_data[current_category] = []
        else:
            seed_data[current_category].append(list(int(value) for value in line.split(' ')))
    return seed_data


def get_seed_ranges(seeds):
    seed_ranges = []
    for i in range(0, len(seeds) - 1, 2):
        first_seed = int(seeds[i])
        second_seed = int(seeds[i + 1])
        seed_pair = (first_seed, second_seed)
        seed_range = [seed_pair[0], seed_pair[0] + seed_pair[1] - 1]
        seed_ranges.append(seed_range)
    return seed_ranges


def get_map_ranges(seed_data):
    reversed_map_list = list(seed_data.keys())[1:]
    reversed_map_list.reverse()
    map_ranges = {}
    for map_name in reversed_map_list:
        map_ranges[map_name] = {}
    for map_name in reversed_map_list:
        map_ranges[map_name]['ranges'] = []
        for map_range in seed_data[map_name]:
            d_start = map_range[0]
            s_start = map_range[1]
            r_length = map_range[2]
            d_end = d_start + r_length - 1
            s_end = s_start + r_length - 1
            m_range = [d_start, d_end, s_start, s_end, r_length]
            map_ranges[map_name]['ranges'].append(m_range)
    return map_ranges


def equation(location, ranges):
    d_start, d_end, s_start, s_end, r_length = ranges
    offset = d_end - location
    answer = s_end - offset
    print(f'{s_end} - ({d_end} - {location}) = {answer}')
    return answer


def should_skip(answer, ranges):
    d_start, d_end, s_start, s_end, r_length = ranges
    if not s_start <= answer <= s_end:
        return True
    return False


def is_seed(potential_seed, seed_range):
    s_start, s_end = seed_range
    if s_start <= potential_seed <= s_end:
        return True
    return False

def main():
    puzzle_input = read_input('part_2_puzzle_5_input.txt')
    seed_data = parse_data(puzzle_input)
    # print(json.dumps(seed_data, indent=4))
    # print('')
    seeds = seed_data['seeds']
    seed_ranges = get_seed_ranges(seeds)
    print(seed_ranges)
    print('')
    map_ranges = get_map_ranges(seed_data)
    print(json.dumps(map_ranges, indent=4))
    print('')
    seed_maps = list(map_ranges.keys())
    print(seed_maps)

    starting_location = -1
    found_seed = False
    while not found_seed:
        starting_location += 1
        location = starting_location
        for mapping in seed_maps:
            print(location)
            print(mapping)
            for r in map_ranges[mapping]['ranges']:
                print(r)
                potential_seed = equation(location, r)
                print(potential_seed)
                if not should_skip(potential_seed, r):
                    location = potential_seed
                    break

        for seed_range in seed_ranges:
            print(potential_seed, seed_range)
            if is_seed(potential_seed, seed_range):
                print(True)
                found_seed = True
                break
            else:
                print(False)
        location += 1
    print(starting_location)


if __name__ == '__main__':
    main()
