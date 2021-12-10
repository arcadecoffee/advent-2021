"""
Advent of Code 2021 - Day 10
https://adventofcode.com/2021/day/10
"""

from typing import List, Union

DAY = 10

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'

closing_symbols = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

unexpected_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def load_data(infile_path: str) -> List[str]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            data.append(line.strip())
    return data


def check_line(line: str) -> [bool, Union[str, List[str]], str]:
    stack = []
    for c in line:
        if c in closing_symbols:
            stack.append(c)
        elif c == closing_symbols[stack[-1]]:
            stack.pop()
        else:
            return False, stack.pop(), c
    return True, [closing_symbols[i] for i in reversed(stack)], None


def part_1(infile_path: str, verbose: bool = False) -> int:
    score = 0
    for line in load_data(infile_path):
        valid, expected, found = check_line(line)
        if not valid:
            if verbose:
                print(f'{line} - Expected {expected}, but found {found} instead.')
            score += unexpected_points[found]
    return score


def part_2(infile_path: str, verbose: bool = False) -> int:
    scores = []
    for line in load_data(infile_path):
        valid, completion, _ = check_line(line)
        if valid:
            score = 0
            for character in completion:
                score = (score * 5) + completion_points[character]
            scores.append(score)
            if verbose:
                print(f'{line} - Complete by adding {"".join(completion)} - {score} total points.')
    return sorted(scores)[int(len(scores)/2)]


if __name__ == '__main__':  # pragma: no cover
    print(f'Part 1: {part_1(FULL_INPUT_FILE)}')
    print(f'Part 2: {part_2(FULL_INPUT_FILE)}')
