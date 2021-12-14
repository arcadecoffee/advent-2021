"""
Advent of Code 2021 - Day 14
https://adventofcode.com/2021/day/14
"""

from collections import Counter
from typing import List, Tuple, Dict, Any

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


def pair_expander(left: str, right: str, rules: Dict[str, str], steps: int):
    if steps == 0:
        yield right
    else:
        yield from pair_expander(left, rules[left + right], rules, steps - 1)
        yield from pair_expander(rules[left + right], right, rules, steps - 1)


def template_expander(infile_path: str, steps: int):
    template, rules = load_data(infile_path)
    yield template[0]
    for i in range(1, len(template)):
        yield from pair_expander(template[i - 1], template[i], rules, steps)


def part_1(infile_path: str) -> int:
    counts = Counter(template_expander(infile_path, 10))
    return max(counts.values()) - min(counts.values())


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
