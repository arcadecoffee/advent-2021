"""
Advent of Code 2021 - Day 15
https://adventofcode.com/2021/day/15
"""

from queue import PriorityQueue
from typing import List

DAY = 15

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[List[int]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append([int(i) for i in line.strip()])
    return data


def find_path(data: List[List[int]]) -> int:
    max_pos = len(data) - 1

    queue = PriorityQueue()
    queue.put([0, 0, 0])
    visited = {}

    while queue:
        score, x, y = queue.get()
        if (x, y) == (max_pos, max_pos):
            return score
        elif (x, y) not in visited:
            for x_offset, y_offset in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= x_offset <= max_pos and 0 <= y_offset <= max_pos:
                    queue.put([score + data[x_offset][y_offset], x_offset, y_offset])
            visited[(x, y)] = True


def embiggen_data(data: List[List[int]], scale: int) -> List[List[int]]:
    size = len(data)
    full_data = []
    for _ in range(size * scale):
        full_data.append([0] * size * scale)
    for i in range(size * scale):
        for k in range((size * scale)):
            full_data[i][k] = int(i / size) + int(k / size) + data[i % size][k % size]
            full_data[i][k] -= 9 if full_data[i][k] > 9 else 0
    return full_data


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return find_path(data)


def part_2(infile_path: str) -> int:
    data = embiggen_data(load_data(infile_path), 5)
    return find_path(data)


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
