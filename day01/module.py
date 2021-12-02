"""
Advent of Code 2021 - Day 1
https://adventofcode.com/2021/day/1
"""

DAY = 1

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def count_increases(infile_path: str, window_size: int) -> int:
    """
    Calculate instances of value increases over windows of the specified size
    :param infile_path: file path to input file with integer values separated by newlines
    :type infile_path: str
    :param window_size: number of values to use when looking for increases during the input series
    :type window_size: int
    :return: count of 'increases' in values in the input file
    :rtype: int
    """
    increases = 0
    with open(infile_path, 'r', encoding='ascii') as data:
        prev_set = [int(next(data)) for _ in range(window_size)]
        for val in data:
            curr_set = prev_set[1:] + [int(val)]
            increases += int(sum(curr_set) > sum(prev_set))
            prev_set = curr_set
    return increases


if __name__ == '__main__':  # pragma: no cover
    part1_answer = count_increases(FULL_INPUT_FILE, 1)
    print(f'Part 1: {part1_answer}')

    part2_answer = count_increases(FULL_INPUT_FILE, 3)
    print(f'Part 2: {part2_answer}')
