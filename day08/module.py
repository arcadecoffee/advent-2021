"""
Advent of Code 2021 - Day 8
https://adventofcode.com/2021/day/8
"""
import statistics
from typing import Dict, List, Set, Union

DAY = 8

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> List[str]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append(line.strip())
    return data

def deduce_dictionary(primer_string: str) -> Dict[int, Set]:
    dictionary = {}
    coded_digits = [set(i) for i in  primer_string.split(' ')]

    dictionary[1] = [i for i in coded_digits if len(i) == 2][0]
    dictionary[4] = [i for i in coded_digits if len(i) == 4][0]
    dictionary[7] = [i for i in coded_digits if len(i) == 3][0]
    dictionary[8] = [i for i in coded_digits if len(i) == 7][0]
    coded_digits = [i for i in coded_digits if i not in dictionary.values()]

    dictionary[3] = [i for i in coded_digits if len(i - dictionary[1]) == 3][0]
    dictionary[6] = [i for i in coded_digits if len(i - dictionary[1]) == 5][0]
    coded_digits = [i for i in coded_digits if i not in dictionary.values()]

    dictionary[0] = [i for i in coded_digits if len(i - dictionary[3]) == 2][0]
    coded_digits.remove(dictionary[0])

    dictionary[9] = [i for i in coded_digits if len(i) == 6][0]
    coded_digits.remove(dictionary[9])

    dictionary[2] = [i for i in coded_digits if len(i - dictionary[9]) == 1][0]
    dictionary[5] = [i for i in coded_digits if len(i - dictionary[9]) == 0][0]

    return dictionary


def decode_message(coded_line: str) -> str:
    primer_string, message_string = coded_line.split(' | ')
    message = ''

    dictionary = deduce_dictionary(primer_string)

    for i in message_string.split(' '):
        message += str([k for k in dictionary if dictionary[k] == set(i)][0])

    return message


def part_1(infile_path: str) -> int:
    count = 0
    input_data = load_data(infile_path)
    for line in input_data:
        message = decode_message(line)
        for c in message:
            if c in '1478':
                count += 1
    return count


def part_2(infile_path: str) -> int:
    message_sum = 0
    input_data = load_data(infile_path)
    for line in input_data:
        message = decode_message(line)
        message_sum += int(message)
    return message_sum


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {part_1(FULL_INPUT_FILE)}')
    print(f'Part 2: {part_2(FULL_INPUT_FILE)}')
