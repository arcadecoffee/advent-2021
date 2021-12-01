"""
Advent of Code 2021 - Day 1
https://adventofcode.com/2021/day/1
"""


def part1(infile: str) -> int:
    """
    Day 1, Part 1
    :param infile: file path to input file with integer values separated by newlines
    :type infile: str
    :return: count of 'increases' in values in the input file
    :rtype: int
    """
    increases = 0

    with open(infile, 'r', encoding='ascii') as data:
        prev = int(next(data))
        for curr in data:
            curr = int(curr)
            increases += int(curr > prev)
            prev = curr

    return increases


def part2(infile: str) -> int:
    """
    Day 1, Part 2
    :param infile: file path to input file with integer values separated by newlines
    :type infile: str
    :return: count of 'increases' in values in the input file
    :rtype: int
    """
    increases = 0

    with open(infile, 'r', encoding='ascii') as data:
        prev_set = [int(next(data)) for _ in range(3)]
        for val in data:
            curr_set = prev_set[1:] + [int(val)]
            increases += int(sum(curr_set) > sum(prev_set))
            prev_set = curr_set

    return increases


def main() -> None:
    """
    Invoke parts 1 & 2
    """
    infile = 'input.txt'
    print(f'Part 1: {part1(infile)}')
    print(f'Part 2: {part2(infile)}')


if __name__ == '__main__':
    main()
