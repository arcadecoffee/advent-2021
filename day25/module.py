"""
Advent of Code 2021 - Day 25
https://adventofcode.com/2021/day/25
"""

from copy import deepcopy
from typing import List, Optional

DAY = '25'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'


class CucumberMap:
    def __init__(self, initial_map: List[List[str]]) -> None:
        self.map = initial_map

    def move_cucumbers(self) -> bool:
        moved = False

        # move east
        new_map: List = deepcopy(self.map)
        for row_num in range(len(self.map)):
            for i in range(len(self.map[row_num])):
                next_i = i + 1 if i + 1 < len(self.map[row_num]) else 0
                if self.map[row_num][i] == '>' and not self.map[row_num][next_i]:
                    new_map[row_num][next_i] = '>'
                    new_map[row_num][i] = None
                    moved = True
        self.map = new_map

        # move south
        new_map = deepcopy(self.map)
        for row_num in range(len(self.map)):
            next_row_num = row_num + 1 if row_num + 1 < len(self.map) else 0
            for col_num in range(len(self.map[row_num])):
                if self.map[row_num][col_num] == 'v' and not self.map[next_row_num][col_num]:
                    new_map[row_num][col_num] = None
                    new_map[next_row_num][col_num] = 'v'
                    moved = True

        self.map = new_map
        return moved

    def dump(self):
        for r in self.map:
            print(''.join([c if c else '.' for c in r]))

    def move_and_dump(self):
        self.move_cucumbers()
        self.dump()


def load_data(infile_path: str) -> List[List[Optional[str]]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append([p if p != '.' else None for p in line.strip()])
    return data


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    i = 1
    cm = CucumberMap(data)
    while cm.move_cucumbers():
        i += 1
    return i


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    part1_answer = part_1(TEST_INPUT_FILE)
#    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

#    part2_answer = part_2(FULL_INPUT_FILE)
#    print(f'Part 2: {part2_answer}')
