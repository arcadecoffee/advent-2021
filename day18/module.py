"""
Advent of Code 2021 - Day 18
https://adventofcode.com/2021/day/18
"""

import re
from math import ceil, floor
from typing import List, Union

DAY = 18

FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'
TEST_INPUT_FILE_1 = f'../inputs/day{DAY:02d}/input.test1.txt'
TEST_INPUT_FILE_2 = f'../inputs/day{DAY:02d}/input.test2.txt'


class SnailFish:
    def __init__(self, left: Union[int, any], right: Union[int, any],
                 depth: int = 0) -> None:
        self.left = left
        self.right = right
        self.depth = depth

    @property
    def magnitude(self) -> int:
        l = self.left if type(self.left) == int else self.left.magnitude
        r = self.right if type(self.right) == int else self.right.magnitude
        return (3 * l) + (2 * r)

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

            left_string_part_match = re.match(r'(.*\D)(\d+)(\D+)', left_string)
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
    return string


def split(string: str) -> str:
    number_match = re.match(r'(.*?\D)(\d{2,})(\D.*)', string)
    if number_match:
        left_string, number, right_string = number_match.groups()
        split_number = f'[{floor(int(number) / 2)},{ceil(int(number) / 2)}]'
        return f'{left_string}{split_number}{right_string}'
    return string


def reduce(string: str) -> str:
    while True:
        new_string = explode(string)
        if string == new_string:
            new_string = split(string)
            if string == new_string:
                return string
        string = new_string


def add(left_string: str, right_string: str) -> str:
    return f'[{left_string},{right_string}]'


def sum_list(data: List[str]) -> str:
    string = data[0]
    for row in data[1:]:
        string = add(string, row)
        string = reduce(string)
    return string


def load_data(infile_path: str) -> List[str]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [i.strip() for i in infile]


def sum_file(infile_path: str) -> str:
    return sum_list(load_data(infile_path))


def calculate_magnitude(string: str) -> int:
    snailfish = SnailFish.parse_snailfish(string)
    return snailfish.magnitude


def part_1(infile_path: str) -> int:
    return SnailFish.parse_snailfish(sum_file(infile_path)).magnitude


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
