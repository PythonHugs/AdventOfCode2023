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


def get_range_maps(seed_maps, map_ranges):
    range_maps = {}
    for mapping in seed_maps:
        print(mapping)
        d_range = []
        for r in map_ranges[mapping]['ranges']:
            d_start, d_end, s_start, s_end, r_length = r
            d_range.append([d_start, d_end, d_start - s_start])
        range_maps[mapping] = {}
        range_maps[mapping]['d_range'] = d_range
    return range_maps


def search(target, range_maps, map_keys):
    d_range = range_maps[map_keys[0]]['d_range']
    for r in d_range:
        # print(r)
        d_start, d_end, offset = r
        if d_start <= target <= d_end:
            new_target = target - offset
            if len(map_keys) == 1:
                return new_target
            return search(new_target, range_maps, map_keys[1:])
    if len(map_keys) == 1:
        return target
    return search(target, range_maps, map_keys[1:])


def main():
    puzzle_input = read_input('part_2_puzzle_5_input.txt')
    seed_data = parse_data(puzzle_input)
    # print(json.dumps(seed_data, indent=4))
    # print('')
    seeds = seed_data['seeds']
    seed_ranges = get_seed_ranges(seeds)
    print(seed_ranges)
    print('')

    min_seeds = []
    for sr in seed_ranges:
        min_seeds.append(sr[0])
    min_seeds.sort()
    print(min_seeds)

    map_ranges = get_map_ranges(seed_data)
    print(json.dumps(map_ranges, indent=4))
    print('')
    seed_maps = list(map_ranges.keys())
    print(seed_maps)

    range_maps = get_range_maps(seed_maps, map_ranges)
    print(range_maps)

    location = 0
    seed_found = False
    while not seed_found:
        print(location)
        seed = search(location, range_maps, seed_maps)
        for r in seed_ranges:
            if r[0] <= seed <= r[-1]:
                seed_found = True
        location += 1
    print(seed_found, location - 1)


if __name__ == '__main__':
    main()
