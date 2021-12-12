"""
Advent of Code 2021 - Day 13
https://adventofcode.com/2021/day/13
"""

from typing import List

DAY = 13

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[List[str]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append(line.strip().split('-'))
    return data


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
