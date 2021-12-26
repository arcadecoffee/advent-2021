"""
Advent of Code 2021 - Day 23
https://adventofcode.com/2021/day/23
"""

from collections import defaultdict
from copy import deepcopy
from queue import PriorityQueue
from typing import Dict, List, Tuple

DAY = '23'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'

PART_1_TEST_MAP = {
    'H': [None] * 7,
    'A': ['B', 'A'],
    'B': ['C', 'D'],
    'C': ['B', 'C'],
    'D': ['D', 'A'],
}

PART_1_FULL_MAP = {
    'H': [None] * 7,
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'A'],
}


class Burrow:
    AMPHIPOD_TYPES = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    PATHS = {
        0: {
            'A': [0, 1],          # 3
            'B': [0, 1, 2],       # 5
            'C': [0, 1, 2, 3],    # 7
            'D': [0, 1, 2, 3, 4], # 9  2n - 1
        },
        1: {
            'A': [1],             # 2
            'B': [1, 2],          # 4
            'C': [1, 2, 3],       # 6
            'D': [1, 2, 3, 4],    # 9  2n
        },
        2: {
            'A': [2],             # 2
            'B': [2],             # 2
            'C': [2, 3],          # 4
            'D': [2, 3, 4],       # 6  2n
        },
        3: {
            'A': [3, 2],          # 4
            'B': [3],             # 2
            'C': [3],             # 2
            'D': [3, 4],          # 4  2n
        },
        4: {
            'A': [4, 3, 2],       # 6
            'B': [4, 3],          # 4
            'C': [4],             # 2
            'D': [4],             # 2  2n
        },
        5: {
            'A': [5, 4, 3, 2],    # 8
            'B': [5, 4, 3],       # 6
            'C': [5, 4],          # 3
            'D': [5],             # 2  2n
        },
        6: {
            'A': [6, 5, 4, 3, 2], # 9
            'B': [6, 5, 4, 3],    # 7
            'C': [6, 5, 4],       # 5
            'D': [6, 5],          # 3 2n - 1
        },
    }

    def __init__(self, state: Dict = None, cost: int = 0):
        self.state = deepcopy(state) if state else {}
        self.cost = cost
        self.state_hash = self._state_hash

    def __lt__(self, other):
        return self.cost < other.cost

    @property
    def _state_hash(self):
        return hash(tuple((k, tuple(v)) for k, v in sorted(self.state.items())))

    def move(self, from_area: str, from_pos: int, to_area: str, to_pos: int):
        if self.state[to_area][to_pos] or from_area == to_area or \
                to_area not in (self.state[from_area][from_pos], 'H'):
            raise ValueError(f'Invalid move from {from_area}-{from_pos} to {to_area}-{to_pos}')
        else:
            self.state[to_area][to_pos] = self.state[from_area][from_pos]
            self.state[from_area][from_pos] = None
            self.state_hash = self._state_hash

    @property
    def is_a_winner(self):
        for amphipod_type in self.AMPHIPOD_TYPES:
            if not all(_ == amphipod_type for _ in self.state[amphipod_type]):
                return False
        return True

    def room_open(self, room: str) -> bool:
        return all(_ in (None, room) for _ in self.state[room])

    def next_spot_in_room(self, room: str) -> int:
        return len(self.state[room]) - 1 - self.state[room][::-1].index(None)

    def path_to_room_clear(self, hallway_start: int, end_room_type: str) -> bool:
        for position in self.PATHS[hallway_start][end_room_type]:
            if position != hallway_start and self.state['H'][position]:
                return False
        return True

    @classmethod
    def move_cost(cls, hallway_position: int, room_type: str, room_position: int,
                  amphipod_type: str):
        hallway_length = 2 * len(cls.PATHS[hallway_position][room_type])
        hallway_length -= 1 if hallway_position in (0, 6) else 0
        return (hallway_length + room_position) * cls.AMPHIPOD_TYPES[amphipod_type]

    @property
    def possible_moves(self) -> List:
        next_possible_states = []
        for hall_pos in range(len(self.state['H'])):
            amphipod_type = self.state['H'][hall_pos]
            if amphipod_type and self.room_open(amphipod_type):
                if self.path_to_room_clear(hall_pos, amphipod_type):
                    room_pos = self.next_spot_in_room(amphipod_type)
                    new_burrow = deepcopy(self)
                    new_burrow.move('H', hall_pos, amphipod_type, room_pos)
                    new_burrow.cost += self.move_cost(hall_pos, amphipod_type, room_pos,
                                                      amphipod_type)
                    return [new_burrow]
        for room in self.AMPHIPOD_TYPES:
            if not self.room_open(room):
                amphipod_type = [_ for _ in self.state[room] if _][0]
                room_pos = self.state[room].index(amphipod_type)
                for hall_pos in self.PATHS:
                    if not self.state['H'][hall_pos] and self.path_to_room_clear(hall_pos, room):
                        new_burrow = Burrow(self.state, self.cost)
                        new_burrow.move(room, room_pos, 'H', hall_pos)
                        new_burrow.cost += self.move_cost(hall_pos, room, room_pos, amphipod_type)
                        next_possible_states.append(new_burrow)
        return next_possible_states


def find_path(burrow: Burrow) -> Burrow:
    queue = PriorityQueue()
    queue.put(burrow)
    visited = defaultdict(bool)

    while queue:
        burrow = queue.get()
        if burrow.is_a_winner:
            return burrow
        elif not visited[burrow.state_hash]:
            print(f'{burrow.cost}', end='\r')
            for possible_move in burrow.possible_moves:
                queue.put(possible_move)
            visited[burrow.state_hash] = True


def load_data(infile_path: str) -> str:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return infile.readline().strip()


def part_1(start_map: Dict) -> int:
    result = find_path(Burrow(start_map))
    return result.cost


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return 0


def show_moves(b):
    for i in range(len(b)):
        print(f'{i} : {b[i].cost} : {b[i].state}')


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
