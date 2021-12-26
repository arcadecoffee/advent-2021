"""
Advent of Code 2021 - Day 24
https://adventofcode.com/2021/day/24
"""

from typing import Any, List

DAY = '24'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST1_INPUT_FILE = f'../inputs/day{DAY}/input.test1.txt'
TEST2_INPUT_FILE = f'../inputs/day{DAY}/input.test2.txt'
TEST3_INPUT_FILE = f'../inputs/day{DAY}/input.test3.txt'


def load_data(infile_path: str) -> List[str]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return [l.strip() for l in infile.readlines()]


class ArithmeticLogicUnitRegister:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return getattr(obj, '_registers')[self.name]

    def __set__(self, obj, value):
        getattr(obj, '_registers')[self.name] = value


class ArithmeticLogicUnit:
    w = ArithmeticLogicUnitRegister()
    x = ArithmeticLogicUnitRegister()
    y = ArithmeticLogicUnitRegister()
    z = ArithmeticLogicUnitRegister()

    def __init__(self, w: int = 0, x: int = 0, y: int = 0, z: int = 0):
        self._registers = {'w': w, 'x': x, 'y': y, 'z': z}

    def execute(self, instructions: List[str], inputs: List[int] = None):
        operations = {
            'inp': lambda a, b: inputs.pop(0),
            'add': lambda a, b: self._registers[a] + b,
            'mul': lambda a, b: self._registers[a] * b,
            'div': lambda a, b: int(self._registers[a] / b),
            'mod': lambda a, b: self._registers[a] % b,
            'eql': lambda a, b: int(self._registers[a] == b)
        }

        for instruction in instructions:
            operation, arg_a, arg_b = (instruction + ' 0').split(' ')[:3]
            arg_b = self._registers[arg_b] if arg_b.isalpha() else int(arg_b)
            self._registers[arg_a] = (operations[operation])(arg_a, arg_b)


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    aaaa = ArithmeticLogicUnit()
    aaaa.execute(['inp x', 'mul x -1'], [42])
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
