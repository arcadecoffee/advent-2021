"""
Advent of Code 2021 - Day 18
https://adventofcode.com/2021/day/18
"""

import re
from typing import Union

DAY = 18

FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


class SnailFish:
    def __init__(self, left: Union[int, any], right: Union[int, any],
                 depth: int = 0) -> None:
        self.left = left
        self.right = right
        self.depth = depth

    @classmethod
    def parse_snailfish(cls, snailfish_string: str, depth: int = 0):
        if snailfish_string.isdigit():
            return int(snailfish_string)
        else:
            bracket_depth = 0
            for i in range(len(snailfish_string)):
                if snailfish_string[i] == '[':
                    bracket_depth += 1
                elif snailfish_string[i] == ']':
                    bracket_depth -= 1
                elif snailfish_string[i] == ',' and bracket_depth == 1:
                    return SnailFish(cls.parse_snailfish(snailfish_string[1:i], depth + 1),
                                     cls.parse_snailfish(snailfish_string[i + 1: -1], depth + 1),
                                     depth + 1)


def explode(string: str) -> str:
    depth = 0
    for i in range(len(string)):
        depth += 1 if string[i] == '[' else -1 if string[i] == ']' else 0
        if depth == 5:
            pair_match = re.match(r'\[(\d+),(\d+)](.*)', string[i:])
            left_string = string[:i]
            left_number, right_number, right_string = pair_match.groups()

            left_string_part_match = re.match(r'(.*\D)(\d+)(\D)', left_string)
            if left_string_part_match:
                new_left, new_number, new_right = left_string_part_match.groups()
                new_number = int(left_number) + int(new_number)
                left_string = f'{new_left}{new_number}{new_right}'

            right_string_part_match = re.match(r'(\D+)(\d+)(\D.*)', right_string)
            if right_string_part_match:
                new_left, new_number, new_right = right_string_part_match.groups()
                new_number = int(right_number) + int(new_number)
                right_string = f'{new_left}{new_number}{new_right}'

            return f'{left_string}0{right_string}'


def add(left_string: str, right_string: str) -> str:
    return f'[{left_string},{right_string}]'


def load_data(infile_path: str) -> str:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return infile.readline().strip()


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
