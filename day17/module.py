"""
Advent of Code 2021 - Day 17
https://adventofcode.com/2021/day/17
"""
import re

from math import ceil, sqrt
from typing import List, Tuple

DAY = 17

FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'


def load_data(infile_path: str) -> Tuple[int, int, int, int]:
    regex = r'target area: x=(-?\d*)\.\.(-?\d*), y=(-?\d*)\.\.(-?\d*)'
    with open(infile_path, 'r', encoding='ascii') as infile:
        x1, x2, y1, y2 = [int(i) for i in re.match(regex, infile.readline()).groups()]
        return x1, x2, y1, y2


def maximum_altitude(y: int) -> int:
    return int(y * -1 * (y * -1 - 1) / 2)


def shot_good(x_velocity: int, y_velocity: int, x1: int, x2: int, y1: int, y2: int) -> bool:
    x_position = y_position = 0
    while x_position <= x2 and y_position >= y1:
        if x_position >= x1 and y_position <= y2:
            return True
        x_position += x_velocity
        y_position += y_velocity
        x_velocity -= 1 if x_velocity else 0
        y_velocity -= 1
    return False


def count_good_shots(x1: int, x2: int, y1: int, y2: int) -> int:
    x_min = ceil(sqrt(x1 * 8 + 1) / 2 - 1 / 2)
    x_max = round(x2 / 2) + 1
    y_min = y1
    y_max = y1 * -1
    arcing_good_shots = []
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            if shot_good(x, y, x1, x2, y1, y2):
                arcing_good_shots.append((x, y))
    direct_shot_count = (x2 + 1 - x1) * (y2 + 1 - y1)
    return len(arcing_good_shots) + direct_shot_count


def part_1(infile_path: str) -> int:
    target_area = load_data(infile_path)
    return maximum_altitude(target_area[2])


def part_2(infile_path: str) -> int:
    target_area = load_data(infile_path)
    return count_good_shots(*target_area)


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
