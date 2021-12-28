"""
Advent of Code 2021 - Day 24
https://adventofcode.com/2021/day/24
"""

from collections import defaultdict
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
        inputs = inputs.copy() if inputs else []
        operations = {
            'inp': lambda a, b: int(inputs.pop(0)),
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


def check_version_number(instructions: List[str], version_number: int):
    alu = ArithmeticLogicUnit()
    alu.execute(instructions, [int(d) for d in list(str(version_number))])
    return not alu.z


def working_area(infile_path: str) -> int:
    instruction_sets = []
    for instruction in load_data(infile_path):
        if instruction.startswith('inp'):
            instruction_sets.append([])
        instruction_sets[-1].append(instruction)

    alu = ArithmeticLogicUnit()
    version_number = 13161151139617
    inputs = [int(d) for d in list(str(version_number))]
    instructions = [i for s in instruction_sets for i in s]
    alu.execute(instructions, inputs)

    return alu.z
    # ## This searches for max input for unique outputs....slows down after a while....
    # z_states_1 = defaultdict(int)
    # search_size = 5
    # for inputs in [list(str(i)) for i in
    #                range(10 ** search_size - 1, 10 ** (search_size - 1) - 1, -1)
    #                if '0' not in str(i)]:
    #     instructions = [i for s in instruction_sets[:search_size] for i in s]
    #     alu = ArithmeticLogicUnit()
    #     alu.execute(instructions, inputs)
    #     z_states_1[alu.z] = max(int(''.join(inputs)), z_states_1[alu.z])
    #
    # ## This searches backwards....meh
    # clues = defaultdict(dict)
    # for z in range(10):
    #     for i in range(1, 10):
    #         alu = ArithmeticLogicUnit(z=z)
    #         alu.execute(instruction_sets[13], [i])
    #         if alu.z == 0:
    #             clues[13][z] = {'z_out': alu.z, 'inp': i}
    #
    # for digit in range(12, 0 - 1, -1):
    #     for z in range(200000):
    #         for i in range(1, 10):
    #             alu = ArithmeticLogicUnit(z=z)
    #             alu.execute(instruction_sets[digit], [i])
    #             if alu.z in clues[digit + 1]:
    #                 clues[digit][z] = {'z_out': alu.z, 'inp': i}


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return working_area(infile_path)


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
