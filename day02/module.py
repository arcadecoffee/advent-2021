"""
Advent of Code 2021 - Day 2
https://adventofcode.com/2021/day/2
"""

DAY = 2

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def calculate_position_part1(infile_path: str) -> int:
    """
    Read input, determine vertical and horizontal position and return the product of the values
    :param infile_path: file path to input file with instructions separated by newlines
    :type infile_path: str
    :return: product of the vertical and horizontal position
    :rtype: int
    """
    horizontal = 0
    vertical = 0
    with open(infile_path, 'r', encoding='ascii') as commands:
        for command in commands:
            direction, units = command.split(' ')
            units = int(units)
            if direction == 'forward':
                horizontal += units
            elif direction == 'down':
                vertical += units
            elif direction == 'up':
                vertical -= units
            else:
                raise ValueError(f'bad command: "{command}"')
    return horizontal * vertical


def calculate_position_part2(infile_path: str) -> int:
    """
    Read input, determine vertical and horizontal position and return the product of the values
    :param infile_path: file path to input file with instructions separated by newlines
    :type infile_path: str
    :return: product of the vertical and horizontal position
    :rtype: int
    """
    horizontal = 0
    vertical = 0
    aim = 0
    with open(infile_path, 'r', encoding='ascii') as commands:
        for command in commands:
            direction, units = command.split(' ')
            units = int(units)
            if direction == 'forward':
                horizontal += units
                vertical += aim * units
            elif direction == 'down':
                aim += units
            elif direction == 'up':
                aim -= units
            else:
                raise ValueError(f'bad command: "{command}"')
    return horizontal * vertical


if __name__ == '__main__':  # pragma: no cover
    part1_answer = calculate_position_part1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = calculate_position_part2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
