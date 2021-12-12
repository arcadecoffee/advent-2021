"""
Advent of Code 2021 - Day 12
https://adventofcode.com/2021/day/12
"""

from collections import Counter
from typing import List

DAY = 12

TEST_1_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test_1.txt'
TEST_2_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test_2.txt'
TEST_3_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test_3.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[List[str]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append(line.strip().split('-'))
    return data


def find_routes(connections: List[List[str]], location: str, visited: List[str],
                revisit: bool = False) -> List[List[str]]:
    routes = []
    if location == 'end':
        return [['end']]
    else:
        visited += [location]
        if max(Counter([i for i in visited if i.islower()]).values()) == 2:
            revisit = False
        for next_location in [next(filter(lambda l: l != location, i))
                              for i in connections if location in i]:
            if next_location != 'start':
                if next_location.isupper() or next_location not in visited or revisit:
                    new_routes = find_routes(connections, next_location, visited.copy(), revisit)
                    for route in new_routes:
                        routes.append([location] + route)
        return routes


def part_1(infile_path: str) -> int:
    routes = find_routes(load_data(infile_path), 'start', [])
    return len(routes)


def part_2(infile_path: str) -> int:
    routes = find_routes(load_data(infile_path), 'start', [], True)
    return len(routes)


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {part_1(FULL_INPUT_FILE)}')
    print(f'Part 2: {part_2(FULL_INPUT_FILE)}')
