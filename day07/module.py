"""
Advent of Code 2021 - Day 7
https://adventofcode.com/2021/day/7
"""
import statistics
from typing import List

DAY = 7

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[int]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [int(i) for i in infile.readline().strip().split(',')]


def calculate_linear_convergence(infile_path: str) -> int:
    crab_positions = load_data(infile_path)
    target_position = statistics.median_high(crab_positions)
    total_cost = sum([abs(i - target_position) for i in crab_positions])
    return total_cost


def calculate_nonlinear_convergence(infile_path: str) -> int:
    crab_positions = load_data(infile_path)
    target_position_low = int(statistics.mean(crab_positions))
    target_position_high = target_position_low + 1
    total_cost_low = sum([sum(range(abs(i - target_position_low) + 1)) for i in crab_positions])
    total_cost_high = sum([sum(range(abs(i - target_position_high) + 1)) for i in crab_positions])
    return min(total_cost_low, total_cost_high)


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {calculate_linear_convergence(FULL_INPUT_FILE)}')
    print(f'Part 2: {calculate_nonlinear_convergence(FULL_INPUT_FILE)}')
