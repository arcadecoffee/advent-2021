"""
Advent of Code 2021 - Day 3
https://adventofcode.com/2021/day/3
"""
from typing import List

DAY = 3

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def calculate_power_consumption(infile_path: str) -> [int, int, int]:
    """
    Read binary values from input and produce gamma, epsilon, and total values
    :param infile_path: file path to input file with instructions separated by newlines
    :type infile_path: str
    :return: gamma, epsilon, and total values
    :rtype: [int, int, int]
    """
    with open(infile_path, 'r', encoding='ascii') as infile:
        values = infile.read().splitlines()

    value_map = None
    for value in values:
        if not value_map:
            value_map = [0 for _ in range(len(value))]
        value_array = [1 if int(_) else -1 for _ in value]
        value_map = [a + b for a, b in zip(value_map, value_array)]
    gamma = int(''.join(['1' if _ > 0 else '0' for _ in value_map]), 2)
    epsilon = int(''.join(['1' if _ < 0 else '0' for _ in value_map]), 2)
    return gamma, epsilon, gamma * epsilon


def calculate_life_support_rating(infile_path: str, mode: str) -> [int, int, int]:
    """
    Read binary values from input and produce gamma, epsilon, and total values
    :param infile_path: file path to input file with instructions separated by newlines
    :type infile_path: str
    :return: gamma, epsilon, and total values
    :rtype: [int, int, int]
    """
    value_matrix = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for value_string in infile:
            value_string = value_string.strip()
            value_matrix.append([int(_) for _ in value_string])

    for i in range(len(value_matrix[0])):
        if len(value_matrix) == 1:
            break
        if mode == 'oxygen':
            target_value = int([sum(x) for x in zip(*value_matrix)][i] >= len(value_matrix) / 2)
        else:
            target_value = int([sum(x) for x in zip(*value_matrix)][i] < len(value_matrix) / 2)
        new_matrix = []
        for row in value_matrix:
            if row[i] == target_value:
                new_matrix.append(row)
        value_matrix = new_matrix
    return int(''.join(['1' if _ else '0' for _ in value_matrix[0]]), 2)


if __name__ == '__main__':  # pragma: no cover
    _, _, total = calculate_power_consumption(FULL_INPUT_FILE)
    print(f'Part 1: {total}')

    oxygen = calculate_life_support_rating(FULL_INPUT_FILE, 'oxygen')
    co2 = calculate_life_support_rating(FULL_INPUT_FILE, 'co2')
    print(f'Part 2: {oxygen * co2}')
