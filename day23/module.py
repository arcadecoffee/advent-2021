"""
Advent of Code 2021 - Day 23
https://adventofcode.com/2021/day/23
"""

from queue import PriorityQueue
from typing import Dict, List, Tuple

DAY = '23'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'


class Burrow:
    COST_FACTOR = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    MAPS = {
        'PART_1': {
            'h1': {'connections': {'h2': 1}},
            'h2': {'connections': {'h1': 1, 'h4': 2, 'a1': 2}},
            'h4': {'connections': {'h2': 2, 'h6': 2, 'a1': 2, 'b1': 2}},
            'h6': {'connections': {'h4': 2, 'h8': 2, 'b1': 2, 'c1': 2}},
            'h8': {'connections': {'h6': 2, 'h10': 2, 'c1': 2, 'd1': 2}},
            'h10': {'connections': {'h8': 2, 'h11': 1, 'd1': 2}},
            'h11': {'connections': {'h10': 1}},
            'a1': {'connections': {'a2': 1, 'h2': 2, 'h4': 2}},
            'a2': {'connections': {'a1': 1}},
            'b1': {'connections': {'b2': 1, 'h4': 2, 'h6': 2}},
            'b2': {'connections': {'b1': 1}},
            'c1': {'connections': {'c2': 1, 'h6': 2, 'h8': 2}},
            'c2': {'connections': {'c1': 1}},
            'd1': {'connections': {'d2': 1, 'h8': 2, 'h10': 2}},
            'd2': {'connections': {'d1': 1}},
        }
    }

    def __init__(self, state: Tuple, burrow_map: str = 'PART_1'):
        self.spots = self.MAPS[burrow_map]
        self.amphipods = dict((k, v) for k, v in state)

    @property
    def state(self):
        return tuple(sorted(self.amphipods.items()))

    def is_a_winner(self) -> bool:
        return all(self.amphipods[a].startswith(a[0].lower()) for a in self.amphipods)

    def move_amphipod(self, amphipod: str, new_spot: str):
        self.amphipods[amphipod] = new_spot

    def move_options(self, amphipod: str, current_spot: str = None, started: str = None, visited: List[str] = None):
        current_spot = current_spot if current_spot else self.amphipods[amphipod]
        visited = visited + [current_spot] if visited else [current_spot]
        started = started if started else current_spot
        amphipod_type = amphipod[0]
        options = []

        if current_spot[0].upper() == amphipod_type:
            if all(_[0] == amphipod_type for _ in self.amphipods if
                   self.amphipods[_].startswith(amphipod_type.lower())
                   and int(self.amphipods[_][1]) > int(current_spot[1])):
                return options

        for destination in self.spots[current_spot]['connections']:
            if destination not in self.amphipods.values() and destination not in visited:
                cost = self.spots[current_spot]['connections'][destination] * \
                       self.COST_FACTOR[amphipod_type]
                options.append((destination, cost))
                for option in self.move_options(amphipod, destination, started, visited):
                    options.append((option[0], option[1] + cost))
        options = self.filter_option_list(options, visited[0], amphipod_type)
        return options

    def filter_option_list(self, option_list: List[Tuple[str, int]], original_start: str,
                           amphipod_type: str) -> List[Tuple[str, int]]:
        options = sorted(
            [min([_ for _ in option_list if _[0] == r], key=lambda l: l[1]) for r in
             [s for s in set([t[0] for t in option_list])]])
        options = list(filter(lambda x: not x[0].startswith(original_start[0]) and
                              (x[0].startswith(amphipod_type.lower()) or x[0].startswith('h')),
                              options))
        if not [k for k, v in self.amphipods.items()
                if not k.startswith(amphipod_type) and v.startswith(amphipod_type.lower())]:
            home_shots = [_ for _ in options if _[0].startswith(amphipod_type.lower())]
            if home_shots:
                options = [max(home_shots, key=lambda l: l[0])]
        return options


def find_path(burrow: Burrow) -> int:
    queue = PriorityQueue()
    queue.put([0, burrow.state])
    visited = set()

    while queue:
        cost, state = queue.get()
        burrow = Burrow(state)
        if burrow.is_a_winner():
            return cost
        elif burrow.state not in visited:
            for amphipod in burrow.amphipods:
                for move, option_cost in burrow.move_options(amphipod):
                    new_burrow = Burrow(burrow.state)
                    new_burrow.move_amphipod(amphipod, move)
                    queue.put([cost + option_cost, new_burrow.state])
            visited.add(burrow.state)


def load_data(infile_path: str) -> str:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return infile.readline().strip()


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


if __name__ == '__main__':
    xstate = (('A0', 'a2'), ('A1', 'd2'),
             ('B0', 'a1'), ('B1', 'c1'),
             ('C0', 'b1'), ('C2', 'c2'),
             ('D0', 'b2'), ('D2', 'd1'))

    ystate = (('A0', 'a2'), ('A1', 'a1'),
             ('B0', 'b2'), ('B1', 'b1'),
             ('C0', 'c1'), ('C2', 'c2'),
             ('D0', 'd2'), ('D2', 'd1'))

    b = Burrow(xstate)
    x = find_path(b)
    1
    # part1_answer = part_1(FULL_INPUT_FILE)
    # print(f'Part 1: {part1_answer}')
    #
    # part2_answer = part_2(FULL_INPUT_FILE)
    # print(f'Part 2: {part2_answer}')
