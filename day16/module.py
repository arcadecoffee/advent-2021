"""
Advent of Code 2021 - Day 16
https://adventofcode.com/2021/day/16
"""

from enum import Enum
from typing import List, Tuple

DAY = 16

FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


def load_data(infile_path: str) -> str:
    with open(infile_path, 'r', encoding='ascii') as infile:
        return infile.readline().strip()

class Packet:
    def __init__(self, bits: str):
        self.bits = bits
        self.version = int(self.bits[0:3], 2)
        self.type = int(self.bits[3:6], 2)
        self.subpackets = []
        self.size = 6

        if self.type == 4:
            self.value, literal_length = self._parse_literal(bits[6:])
            self.size += literal_length
        else:
            self.length_type = int(self.bits[6:7], 2)
            self.size += 1

            if self.length_type == 0:
                field_size = 15
                subpacket_length = int(self.bits[7:7 + field_size], 2)
                self.size = self.size + field_size + subpacket_length
                self.subpackets = self._parse_all_subpackets(
                    bits[7 + field_size:7 + field_size + subpacket_length]
                )
            else:
                field_size = 11
                subpacket_count = int(self.bits[7:7 + field_size], 2)
                self.size = self.size + field_size
                for _ in range(subpacket_count):
                    self.subpackets.append(Packet(bits[self.size:]))
                    self.size += self.subpackets[-1].size

    @classmethod
    def _parse_all_subpackets(cls, bits: str) -> List[any]:
        packets = []
        while bits:
            packets.append(Packet(bits))
            bits = bits[packets[-1].size:]
        return packets

    @property
    def version_sum(self) -> int:
        subpacket_version_sum = 0
        for subpacket in self.subpackets:
            subpacket_version_sum += subpacket.version_sum
        return self.version + subpacket_version_sum

    @classmethod
    def _parse_literal(cls, bits: str) -> Tuple[int, int]:
        keep_going = True
        value_bits = ''
        length = 0
        while keep_going:
            keep_going = int(bits[0])
            value_bits += bits[1:5]
            bits = bits[5:]
            length += 5
        return int(value_bits, 2), length


def calculate_version_sums(data: str) -> int:
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packet = Packet(bits)
    return packet.version_sum


def part_1(infile_path: str) -> int:
    data = load_data(infile_path)
    return calculate_version_sums(data)


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    return -1


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
