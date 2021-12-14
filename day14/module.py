"""
Advent of Code 2021 - Day 14
https://adventofcode.com/2021/day/14
"""

from collections import Counter
from typing import Tuple, Dict

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


def pair_counter(infile_path: str, steps: int) -> Dict[str, float]:
    template, rules = load_data(infile_path)
    pairs = {}
    counts = {}
    for i in range(1, len(template)):
        pairs[template[i - 1] + template[i]] = pairs.get(template[i - 1] + template[i], 0) + 1

    for i in range(steps):
        new_pairs = {}
        counts = {template[0]: 0.5, template[-1]: 0.5}
        for key, value in pairs.items():
            c = rules[key]
            new_pairs[key[0] + c] = new_pairs.get(key[0] + c, 0) + value
            new_pairs[c + key[1]] = new_pairs.get(c + key[1], 0) + value
            for k in [key[0], key[1], c, c]:
                counts[k] = counts.get(k, 0) + (value / 2)
        pairs = new_pairs
    return counts


def part_1(infile_path: str) -> int:
    counts = pair_counter(infile_path, 10)
    return int(max(counts.values()) - min(counts.values()))


def part_2(infile_path: str) -> int:
    counts = pair_counter(infile_path, 40)
    return int(max(counts.values()) - min(counts.values()))


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
