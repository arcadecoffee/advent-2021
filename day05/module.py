"""
Advent of Code 2021 - Day 5
https://adventofcode.com/2021/day/5
"""
import re
from typing import Dict, List, Union

DAY = 5

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


class VentMap:
    def __init__(self):
        self.map_data = {}
        self.max_x = 0
        self.max_y = 0

    @classmethod
    def calculate_increment(cls, a: int, b: int):
        return 0 if a == b else 1 if a < b else -1

    def increment_point(self, x: int, y: int):
        self.map_data[x] = self.map_data.get(x, {})
        self.map_data[x][y] = self.map_data[x].get(y, 0) + 1
        self.max_x = max([x, self.max_x])
        self.max_y = max([y, self.max_y])

    def add_line(self, x1: int, y1: int, x2: int, y2: int):
        x_increment = VentMap.calculate_increment(x1, x2)
        y_increment = VentMap.calculate_increment(y1, y2)
        while x1 != x2 or y1 != y2:
            self.increment_point(x1, y1)
            x1 += x_increment
            y1 += y_increment
        self.increment_point(x1, y1)

    def find_values(self, target: int) -> List[Dict[str, int]]:
        points = []
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                if self.map_data.get(x, {}).get(y, 0) >= target:
                    points.append({'x': x, 'y': y})
        return points


def load_data(infile_path: str) -> List[Dict[str, int]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for data_row in infile:
            (x1, y1, x2, y2) = re.split(r' -> |,', data_row)
            data.append({'x1': int(x1), 'y1': int(y1), 'x2': int(x2), 'y2': int(y2)})
    return data


def find_straight_lines(data: List[Dict[str, int]]) -> List[Dict[str, int]]:
    straight_lines = []
    for data_row in data:
        if data_row['x1'] == data_row['x2'] or data_row['y1'] == data_row['y2']:
            straight_lines.append(data_row)
    return straight_lines


def count_intersections(infile_path: str, straight_lines_only: bool = True) -> int:
    vent_map = VentMap()
    data = load_data(infile_path)

    if straight_lines_only:
        data = find_straight_lines(data)

    for line in data:
        vent_map.add_line(line['x1'], line['y1'], line['x2'], line['y2'])
    return len(vent_map.find_values(2))


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {count_intersections(FULL_INPUT_FILE)}')
    print(f'Part 2: {count_intersections(FULL_INPUT_FILE, False)}')
