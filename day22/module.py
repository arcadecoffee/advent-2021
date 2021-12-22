"""
Advent of Code 2021 - Day 22
https://adventofcode.com/2021/day/22
"""

import re
from itertools import product
from typing import List, Tuple, Union, Any

DAY = '22'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE_1 = f'../inputs/day{DAY}/input.test1.txt'
TEST_INPUT_FILE_2 = f'../inputs/day{DAY}/input.test2.txt'
TEST_INPUT_FILE_3 = f'../inputs/day{DAY}/input.test3.txt'


def load_data(infile_path: str) -> List[List[Union[str, Any]]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            split_data = \
                re.match(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$',
                         line).groups()
            data.append([split_data[0]] + [int(i) for i in split_data[1:]])
    return data


def part_1(infile_path: str) -> int:
    illuminated = set()
    data = load_data(infile_path)
    for d in data:
        x1, x2, y1, y2, z1, z2 = sorted(d[1:3]) + sorted(d[3:5]) + sorted(d[5:7])
        if not (x1 > 50 or x2 < -50 or y1 > 50 or y2 < -50 or z1 > 50 or z2 < -50):
            d_set = set()
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        d_set.add((x, y, z))
            if d[0] == 'on':
                illuminated.update(d_set)
            if d[0] == 'off':
                illuminated = illuminated - d_set
    return len(illuminated)


def collides(box_a: List[int], box_b: List[int]) -> bool:
    ax1, ax2, ay1, ay2, az1, az2 = sorted(box_a[0:2]) + sorted(box_a[2:4]) + sorted(box_a[4:6])

    for x, y, z in product(box_b[0:2], box_b[2:4], box_b[4:6]):
        if ax1 <= x <= ax2 and ay1 <= y <= ay2 and az1 <= z <= az2:
            return True
    return False


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
