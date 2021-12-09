"""
Advent of Code 2021 - Day 9
https://adventofcode.com/2021/day/9
"""
import math
from typing import Dict, List, Set

DAY = 9

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[List[int]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append([int(i) for i in line.strip()])
    return data


def find_low_points(height_map: List[List[int]]) -> List[Dict[str, int]]:
    num_rows = len(height_map)
    num_columns = len(height_map[0])
    low_points = []
    for i in range(num_rows):
        for j in range(num_columns):
            if (
                    (i - 1 < 0 or height_map[i][j] < height_map[i - 1][j]) and
                    (j - 1 < 0 or height_map[i][j] < height_map[i][j - 1]) and
                    (i + 1 >= num_rows or height_map[i][j] < height_map[i + 1][j]) and
                    (j + 1 >= num_columns or height_map[i][j] < height_map[i][j + 1])
            ):
                low_points.append({'row': i, 'col': j})
    return low_points


def find_low_point_score(infile_path: str) -> int:
    height_map = load_data(infile_path)
    low_points = find_low_points(height_map)
    score = 0
    for low_point in low_points:
        score += 1 + height_map[low_point['row']][low_point['col']]
    return score


def find_basins(infile_path: str) -> List[Set[str]]:
    height_map = load_data(infile_path)
    basins = []
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if height_map[i][j] != 9:
                new_basin = {f'{i},{j}'}
                for basin in basins:
                    if (
                            f'{i - 1},{j}' in basin or
                            f'{i + 1},{j}' in basin or
                            f'{i},{j - 1}' in basin or
                            f'{i},{j + 1}' in basin
                    ):
                        new_basin = new_basin.union(basin)
                        basins.remove(basin)
                basins.append(new_basin)
    return basins


def find_basin_score(infile_path: str) -> int:
    basins = find_basins(infile_path)
    basins.sort(key=len, reverse=True)
    return math.prod(len(i) for i in basins[:3])


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {find_low_point_score(FULL_INPUT_FILE)}')
    print(f'Part 2: {find_basin_score(FULL_INPUT_FILE)}')
