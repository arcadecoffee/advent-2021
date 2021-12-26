"""
Advent of Code 2021 - Day 24
https://adventofcode.com/2021/day/24
"""

from typing import List

DAY = '24'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST1_INPUT_FILE = f'../inputs/day{DAY}/input.test1.txt'
TEST2_INPUT_FILE = f'../inputs/day{DAY}/input.test2.txt'
TEST3_INPUT_FILE = f'../inputs/day{DAY}/input.test3txt'


def load_data(infile_path: str) -> List[str]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [l.strip() for l in infile.readlines()]


class ArithmeticLogicUnit:
    def __init__(self, w: int = 0, x: int = 0, y: int = 0, z: int = 0):
        self._registers = {'w': w, 'x': x, 'y': y, 'z': z}


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
