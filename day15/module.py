"""
Advent of Code 2021 - Day 15
https://adventofcode.com/2021/day/15
"""

from collections import defaultdict
from queue import PriorityQueue
from typing import List, Tuple

DAY = 15

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def diagonals(size: int) -> Tuple[int, int]:
    for i in range(1, size * 2 - 1):
        for j in range(i + 1):
            if i - j < size and j < size:
                yield j, i - j


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
    visited = defaultdict(lambda: False)

    while queue:
        score, x, y = queue.get()
        if (x, y) == (max_pos, max_pos):
            return score
        elif not visited[(x, y)]:
            for x_offset, y_offset in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= x_offset <= max_pos and  0 <= y_offset <= max_pos:
                    queue.put([score + data[x_offset][y_offset], x_offset, y_offset])
            visited[(x, y)] = True


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return find_path(data)


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    full_data = []
    for r in data:
        full_data.append([n + m - 9 if n + m > 9 else n + m for n in range(5) for m in r])
    data = full_data[::]
    for i in range(1, 5):
        full_data.extend([[n + i - 9 if n + i > 9 else n + i for n in m] for m in data])
    return find_path(full_data)


    # for i in range(len(full_data)):
    #     for k in range(len(full_data[i])):
    #         full_data[i][k] = (data[i % len(data)][k % len(data)] + int(i / len(data))) % 9

    # for i in range(5):
    #     full_data.extend([[(n + i) % 9 for n in m] for m in data])
    return -1


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
