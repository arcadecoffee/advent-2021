"""
Advent of Code 2021 - Day 6
https://adventofcode.com/2021/day/6
"""
from typing import Dict, List, Union

DAY = 6

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[int]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [int(i) for i in infile.readline().strip().split(',')]


def find_straight_lines(data: List[Dict[str, int]]) -> List[Dict[str, int]]:
    straight_lines = []
    for data_row in data:
        if data_row['x1'] == data_row['x2'] or data_row['y1'] == data_row['y2']:
            straight_lines.append(data_row)
    return straight_lines


def calculate_births(infile_path: str, days: int) -> [int, List[int]]:
    timeline = [0 for _ in range(days + 9)]

    initial_state = load_data(infile_path)
    for i in initial_state:
        timeline[i] += 1

    for i in range(9 + days):
        n = timeline[i]
        for j in range(i + 9, 9 + days, 7):
            if j < 9 + days:
                timeline[j] += n
    return sum(timeline), timeline


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {calculate_births(FULL_INPUT_FILE, 80)[0]}')
    print(f'Part 1: {calculate_births(FULL_INPUT_FILE, 256)[0]}')
