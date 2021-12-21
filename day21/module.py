"""
Advent of Code 2021 - Day 21
https://adventofcode.com/2021/day/21
"""

import re
from typing import List, Tuple

DAY = '21'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'


def load_data(infile_path: str) -> List[int]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [int(re.search(r'(\d+)$', i).group()) for i in infile]


def calculate_cycles(p1_start: int, p2_start: int) -> Tuple[List[int], List[int]]:
    cycle_length = 10
    cycle_range = range(cycle_length)
    p1_moves, p2_moves = \
        [[((((6 * (i + 1) - j) * 3) - 1) % 10) + 1 for i in cycle_range] for j in (4, 1)]
    p1_cycle, p2_cycle = [[i] * cycle_length for i in (p1_start, p2_start)]
    for i in cycle_range:
        p1_cycle[i] = ((p1_moves[i] - 1 + p1_cycle[i - 1]) % 10) + 1
        p2_cycle[i] = ((p2_moves[i] - 1 + p2_cycle[i - 1]) % 10) + 1
    return p1_cycle, p2_cycle


def calculate_p1_cycle(start: int = 0) -> List[int]:
    cycle_range = range(5)
    p1_moves = [((((6 * (i + 1) - 4) * 3) - 1) % 10) + 1 for i in cycle_range]
    p1_cycle = [start] * 5
    for i in cycle_range:
        p1_cycle[i] = ((p1_moves[i] - 1 + p1_cycle[i - 1]) % 10) + 1
    return p1_cycle


def calculate_p2_cycle(p1_start: int = 0) -> List[int]:
    cycle_range = range(10)
    p2_moves = [((((6 * (i + 1) - 1) * 3) - 1) % 10) + 1 for i in cycle_range]
    p2_cycle = []
    for i in cycle_range:
        prev_position = p1_start if not p2_cycle else p2_cycle[i - 1]
        p2_cycle.append(((p2_moves[i] - 1 + prev_position) % 10) + 1)
    return p2_cycle


def find_winning_turn(target: int, cycle: List[int]) -> int:
    full_cycles = int(target / sum(cycle))
    points = full_cycles * sum(cycle)
    i = 0
    while points < target:
        points += cycle[i]
        i += 1
    return (full_cycles * len(cycle)) + i


def find_score_at_turn(turn: int, cycle: List[int]):
    full_cycles = int(turn / len(cycle))
    points = full_cycles * sum(cycle)
    i = 0
    while (full_cycles * len(cycle)) + i < turn:
        points += cycle[i]
        i += 1
    return points


def part_1(infile_path: str) -> int:
    p1_start, p2_start = load_data(infile_path)
    p1_cycle, p2_cycle = calculate_cycles(p1_start, p2_start)
    p1_winning_turn = find_winning_turn(1000, p1_cycle)
    p2_winning_turn = find_winning_turn(1000, p2_cycle)
    if p1_winning_turn <= p2_winning_turn:
        losing_score = find_score_at_turn(p1_winning_turn - 1, p2_cycle)
        total_rolls = (6 * p1_winning_turn) - 3
    else:
        losing_score = find_score_at_turn(p2_winning_turn, p1_cycle)
        total_rolls = 6 * p2_winning_turn
    return losing_score * total_rolls


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
