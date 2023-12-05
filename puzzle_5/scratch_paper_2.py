""" Part 2 for Puzzle 5 for Advent of Code 2023 """
# https://adventofcode.com/2023/day/5
import asyncio
import concurrent.futures
import multiprocessing
import numpy as np
from functools import partial


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


def math_trick(maps, seed_data, target):
    print('')
    print(target)
    for seed_map in maps:
        print(seed_map)
        ranges = seed_data[seed_map]
        for r in ranges:
            srs = int(seed_data[seed_map][r]['source_range_start'])
            r_length = int(seed_data[seed_map][r]['range_length'])
            r_limit = srs + r_length - 1
            drs = int(seed_data[seed_map][r]['destination_range_start'])
            d_limit = drs + r_length - 1
            if not srs <= target <= r_limit:
                print(f'skipped{r}')
                continue
            if srs <= target <= r_limit:
                diff = r_limit - target
                c = d_limit - diff
                print(target, c)
                # print('')
                if len(maps) == 1:
                    return c
                return math_trick(maps[1:], seed_data, c)
                # maps = maps[1:]
        if len(maps) == 1:
            return target
        return math_trick(maps[1:], seed_data, target)
        # maps = maps[1:]


async def check_array(master_seed_list, math_trick_partial):
    cpu_count = multiprocessing.cpu_count() - 2
    chunks = np.array_split(master_seed_list, cpu_count)
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count)
    tasks = [asyncio.get_running_loop().run_in_executor(executor, check_chunk, chunk, math_trick_partial) for chunk in chunks]
    results = await asyncio.gather(*tasks)
    results = [item for sublist in results for item in sublist]
    return results


def check_chunk(chunk, math_trick_partial):
    pool = multiprocessing.Pool()
    location = pool.map(math_trick_partial, chunk)
    pool.close()
    pool.join()
    return location


def main():
    puzzle_input = read_input('part_2_puzzle_5_input.txt')
    seed_data = parse_data(puzzle_input)
    # print(json.dumps(seed_data, indent=4))

    seeds = seed_data['seeds']
    seed_list = []
    for i in range(0, len(seeds) - 1, 2):
        first_seed = int(seeds[i])
        second_seed = int(seeds[i + 1])
        seed_pair = (first_seed, second_seed)
        seed_list.append(seed_pair)
    print(seed_list)

    maps = list(seed_data.keys())[1:]
    master_seed_list = []
    seed_locations = []
    test_list = [seed_list[0]]
    print(test_list)
    for seed_pair in test_list:
        for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
            master_seed_list.append(seed)
        # print(master_seed_list)
        math_trick_partial = partial(math_trick, maps, seed_data)
        seed_locations.extend(asyncio.run(check_array(master_seed_list, math_trick_partial)))
        print(seed_locations)
        master_seed_list = []
    seed_locations.sort()
    print(seed_locations[0])


if __name__ == '__main__':
    main()
