"""
Advent of Code 2021 - Day ZZ
https://adventofcode.com/2021/day/ZZ
"""

DAY = 'ZZ'

FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'


def load_data(infile_path: str) -> str:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return infile.readline().strip()


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
