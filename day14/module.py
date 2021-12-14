"""
Advent of Code 2021 - Day 14
https://adventofcode.com/2021/day/14
"""

from collections import defaultdict
from itertools import tee
from typing import Tuple, Dict, Iterable

DAY = 14

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> Tuple[str, Dict[str, str]]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        template = infile.readline().strip()
        infile.readline()
        rules = {}
        for line in infile:
            key, value = line.strip().split(' -> ')
            rules[key] = value
    return template, rules


def pair_counter(infile_path: str, steps: int) -> Dict[str, int]:
    template, rules = load_data(infile_path)

    pairs = defaultdict(int)
    a, b = tee(template)
    next(b, None)
    for i, j in zip(a, b):
        pairs[i + j] += 1

    for i in range(steps):
        new_pairs = defaultdict(int)
        for key, value in pairs.items():
            c = rules[key]
            new_pairs[key[0] + c] += value
            new_pairs[c + key[1]] += value
        pairs = new_pairs

    counts = defaultdict(int)
    for k, v in list(pairs.items()) + [(template[0], 1), (template[-1], 1)]:
        for c in k:
            counts[c] += v

    return {k: int(v / 2) for k, v in counts.items()}


def find_answer(infile_path: str, steps: int) -> int:
    counts = pair_counter(infile_path, steps)
    return max(counts.values()) - min(counts.values())


def part_1(infile_path: str) -> int:
    return find_answer(infile_path, 10)


def part_2(infile_path: str) -> int:
    return find_answer(infile_path, 40)


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
