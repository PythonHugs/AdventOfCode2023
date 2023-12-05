""" Part 2 for Puzzle 5 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/5


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
    range_counter = 0
    for line in puzzle_input:
        if line == '':
            range_counter = 0
        elif ':' in line:
            current_category = line.split(':')[0]
            if current_category == 'seeds':
                seed_data[current_category] = line.split(':')[1].split(' ')[1:]
            else:
                seed_data[current_category] = {}

        else:
            seed_data[current_category][f'range_{range_counter}'] = {}
            current_range = seed_data[current_category][f'range_{range_counter}']
            current_range['destination_range_start'] = line.split(' ')[0]
            current_range['source_range_start'] = line.split(' ')[1]
            current_range['range_length'] = line.split(' ')[2]
            range_counter += 1
    return seed_data


def math_trick(target, maps, seed_data):
    for map in maps:
        print(map)
        ranges = seed_data[map]
        for r in ranges:
            print(r)
            drs = int(seed_data[map][r]['destination_range_start'])
            srs = int(seed_data[map][r]['source_range_start'])
            r_length = int(seed_data[map][r]['range_length'])
            r_limit = srs + r_length - 1
            d_limit = drs + r_length - 1
            if not srs <= target <= r_limit:
                print(f'skipped{r}')
                continue
            diff = r_limit - target
            c = d_limit - diff
            print(target, c)
            if len(maps) == 1:
                return c
            return math_trick(c, maps[1:], seed_data)
        if len(maps) == 1:
            return target
        return math_trick(target, maps[1:], seed_data)


def main():
    puzzle_input = read_input('part_2_puzzle_5_input.txt')
    seed_data = parse_data(puzzle_input)
    # print(json.dumps(seed_data, indent=4))

    seeds = seed_data['seeds']
    seed_list = []
    master_seed_list = []
    for i in range(0, len(seeds) - 1, 2):
        first_seed = int(seeds[i])
        second_seed = int(seeds[i + 1])
        seed_pair = (first_seed, second_seed)
        seed_list.append(seed_pair)
        # last_seed = first_seed + int(seeds[i + 1])
        # seed_list = list(range(first_seed, last_seed + 1))
    print(seed_list)
    #     master_seed_list.extend(seed_list)
    # print(master_seed_list)

    # for seed_pair in seed_list:
    #     for x in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
    #         print(x)

    maps = list(seed_data.keys())[1:]
    seed_locations = []
    for seed_pair in seed_list:
        for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
            # for seed in master_seed_list:
            print('')
            print(seed)
            seed_locations.append(math_trick(int(seed), maps, seed_data))
    print(seed_locations)
    seed_locations.sort()
    print(seed_locations[0])


if __name__ == '__main__':
    main()
