"""
Advent of Code 2021 - Day 13
https://adventofcode.com/2021/day/13
"""
import re
from typing import List, Union

DAY = 13

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> [List[List[int]], List[List[Union[str, int]]]]:
    coords = []
    folds = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        line = infile.readline().strip()
        while line:
            coords.append([int(i) for i in line.split(',')])
            line = infile.readline().strip()

        line = infile.readline().strip()
        while line:
            _, axis, value = re.split(r'fold along |=', line)
            folds.append([axis, int(value)])
            line = infile.readline().strip()
    return coords, folds


class DotMap:
    def __init__(self, dots: List[List[int]]):
        self.matrix = {}
        for x, y in dots:
            if not self.matrix.get(y):
                self.matrix[y] = set()
            self.matrix[y].add(x)

    def fold_x(self, n: int):
        for y, xs in self.matrix.items():
            new_xs = set()
            for x in xs:
                new_xs.add(x if x < n else 2 * n - x)
            self.matrix[y] = new_xs

    def fold_y(self, n: int):
        new_matrix = {}
        for y in self.matrix:
            if y > n:
                if not new_matrix.get(2 * n - y):
                    new_matrix[2 * n - y] = self.matrix[y]
                else:
                    new_matrix[2 * n - y].update(self.matrix[y])
            elif y < n:
                if not new_matrix.get(y):
                    new_matrix[y] = self.matrix[y]
                else:
                    new_matrix[y].update(self.matrix[y])
        self.matrix = new_matrix

    def fold(self, axis: str, n: int):
        if axis == 'x':
            self.fold_x(n)
        elif axis == 'y':
            self.fold_y(n)

    @property
    def dot_count(self):
        count = 0
        for i in self.matrix.values():
            count += len(i)
        return count

    @property
    def matrix_display(self):
        display = ''
        width = max(([max(self.matrix[i]) for i in self.matrix])) + 1
        height = max(self.matrix) + 1
        for h in range(height):
            for w in range(width):
                display += '#' if w in self.matrix.get(h) else ' '
            display += '\n'
        return display


def part_1(infile_path: str) -> int:
    coords, folds = load_data(infile_path)
    dotmap = DotMap(coords)
    axis, n = folds[0]
    dotmap.fold(axis, n)
    return dotmap.dot_count


def part_2(infile_path: str) -> int:
    coords, folds = load_data(infile_path)
    dotmap = DotMap(coords)
    for axis, n in folds:
        dotmap.fold(axis, n)
    return dotmap.matrix_display


if __name__ == '__main__':  # pragma: no cover
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: \n{part2_answer}')
