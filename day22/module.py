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


def colliding_corners(box_a: List[int], box_b: List[int]) -> int:
    ax1, ax2, ay1, ay2, az1, az2 = sorted(box_a[0:2]) + sorted(box_a[2:4]) + sorted(box_a[4:6])
    corners = 0
    for x, y, z in product(box_b[0:2], box_b[2:4], box_b[4:6]):
        if ax1 <= x <= ax2 and ay1 <= y <= ay2 and az1 <= z <= az2:
            corners += 1
    return corners


def overlapping_volume(box_a: List[int], box_b: List[int]) -> int:
    ax, axp, ay, ayp, az, azp = box_a
    bx, bxp, by, byp, bz, bzp = box_b
    return max(min(axp + 1, bxp + 1) - max(ax, bx), 0) * \
           max(min(ayp + 1, byp + 1) - max(ay, by), 0) * \
           max(min(azp + 1, bzp + 1) - max(az, bz), 0)


def overlapping_box(box_a: List[int], box_b: List[int]) -> Tuple[int, ...]:
    ax, axp, ay, ayp, az, azp = box_a
    bx, bxp, by, byp, bz, bzp = box_b
    return max(ax, bx), min(axp, bxp), max(ay, by),  min(ayp, byp), max(az, bz), min(azp, bzp)


def count_lit_cubes(data):
    lit_count = 0
    counted_zones = []
    for d in reversed(data):
        mode, box = d[0], d[1:]
        x1, x2, y1, y2, z1, z2 = box
        if mode == 'on':
            dead_cubes = set()
            for zone in counted_zones:
                if overlapping_volume(zone, box):
                    ox1, ox2, oy1, oy2, oz1, oz2 = overlapping_box(zone, box)
                    dead_cubes.update(
                        product(range(ox1, ox2 + 1), range(oy1, oy2 + 1), range(oz1, oz2 + 1)))
            lit_count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            lit_count -= len(dead_cubes)
        counted_zones.append(box)
    return lit_count


def part_1(infile_path:str) -> int:
    data = load_data(infile_path)
    clean_data = []
    for row in data:
        x1, x2, y1, y2, z1, z2 = row[1:]
        if x1 <= 50 and x2 >= -50 and y1 <= 50 and y2 >= -50 and z1 <= 50 and z2 >= -50:
            clean_data.append(row)
    lit_count = count_lit_cubes(clean_data)
    return lit_count


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    lit_count = count_lit_cubes(data)
    return lit_count


if __name__ == '__main__':
    r = part_1_a(TEST_INPUT_FILE_1)
    print(r)
    # part1_answer = part_1(FULL_INPUT_FILE)
    # print(f'Part 1: {part1_answer}')
    #
    # part2_answer = part_2(FULL_INPUT_FILE)
    # print(f'Part 2: {part2_answer}')
