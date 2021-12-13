"""
Advent of Code 2021 - Day 12
https://adventofcode.com/2021/day/12
"""

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


def find_routes(connections: List[List[str]], location: str, previously_visited: List[str] = None,
                revisit: bool = False) -> List[List[str]]:
    routes = []
    if location == 'end':
        routes.append(['end'])
    else:
        visited = previously_visited.copy() if previously_visited else []
        revisit = revisit and (location.isupper() or location not in visited)
        visited.append(location)
        for next_location in \
                [next(filter(lambda l: l != location, i)) for i in connections if location in i]:
            if next_location != 'start' and \
                    (revisit or next_location.isupper() or next_location not in visited):
                new_routes = find_routes(connections, next_location, visited, revisit)
                for route in new_routes:
                    routes.append([location] + route)
    return routes


def part_1(infile_path: str) -> int:
    routes = find_routes(load_data(infile_path), 'start')
    return len(routes)


def part_2(infile_path: str) -> int:
    routes = find_routes(load_data(infile_path), 'start', revisit=True)
    return len(routes)


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {part_1(FULL_INPUT_FILE)}')
    print(f'Part 2: {part_2(FULL_INPUT_FILE)}')
