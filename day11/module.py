"""
Advent of Code 2021 - Day 11
https://adventofcode.com/2021/day/11
"""

from itertools import permutations, product
from typing import List

DAY = 11

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
TEST_SMALL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.small.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


class OctopusSwarm:
    _offsets = set(product([-1, 0, 1], repeat=2)) - {(0,0)}

    def __init__(self, grid: List[List[int]]):
        self.grid = [i[:] for i in grid]
        self.grid_rows = len(grid)
        self.grid_cols = len(grid[0])
        self.flash_count = 0
        self.step_number = 0

    def increment_octopus(self, row: int, col: int) -> bool:
        triggered = False
        if (0 <= row < self.grid_rows) and (0 <= col < self.grid_cols):
            self.grid[row][col] += 1
            triggered = True if self.grid[row][col] == 10 else False
        return triggered

    def cycle_swarm(self, cycles: int = 1):
        for _ in range(cycles):
            triggered = []
            for row, col in product(range(self.grid_rows), range(self.grid_cols)):
                if self.increment_octopus(row, col):
                    triggered.append([row, col])
                    self.flash_count += 1
            while triggered:
                new_triggered = []
                for row, col in triggered:
                    for row_incr, col_incr in OctopusSwarm._offsets:
                        if self.increment_octopus(row + row_incr, col + col_incr):
                            new_triggered.append([row + row_incr, col + col_incr])
                            self.flash_count += 1
                triggered = new_triggered
            for row, col in product(range(self.grid_rows), range(self.grid_cols)):
                if self.grid[row][col] > 9:
                    self.grid[row][col] = 0
            self.step_number += 1

    def full_flash(self) -> bool:
        for row, col in product(range(self.grid_rows), range(self.grid_cols)):
            if self.grid[row][col] != 0:
                return False
        return True


def load_data(infile_path: str) -> List[List[int]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append([int(i) for i in line.strip()])
    return data


def part_1(infile_path: str, steps: int) -> int:
    swarm = OctopusSwarm(load_data(infile_path))
    swarm.cycle_swarm(steps)
    return swarm.flash_count


def part_2(infile_path: str) -> int:
    swarm = OctopusSwarm(load_data(infile_path))
    while not swarm.full_flash():
        swarm.cycle_swarm()
    return swarm.step_number


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {part_1(FULL_INPUT_FILE, 100)}')
    print(f'Part 2: {part_2(FULL_INPUT_FILE)}')
