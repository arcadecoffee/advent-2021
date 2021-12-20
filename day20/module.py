"""
Advent of Code 2021 - Day 20
https://adventofcode.com/2021/day/20
"""

from typing import List, Tuple

DAY = '20'

FULL_INPUT_FILE = f'../inputs/day{DAY}/input.full.txt'
TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'


class Image:
    def __init__(self, algorithm:str, image: List[str]) -> None:
        self._algorithm_bitmap = [c == '#' for c in algorithm]
        self._image_bitmap = [[c == '#' for c in r] for r in image]
        self.background = False

    def add_margin(self, size: int = 1) -> None:
        for row in self._image_bitmap:
            row[0:0] = [self.background] * size
            row[self.width:self.width] = [self.background] * size
        self._image_bitmap[0:0] = [[self.background] * self.width] * size
        self._image_bitmap[self.height:self.height] = [[self.background] * self.width] * size

    def crop(self) -> None:
        while all(c == self.background for c in self._image_bitmap[0]):
            del self._image_bitmap[0]
        while all(c == self.background for c in self._image_bitmap[-1]):
            del self._image_bitmap[-1]
        while all(c == self.background for c in [r[0] for r in self._image_bitmap]):
            for s in self._image_bitmap:
                del s[0]
        while all(c == self.background for c in [r[-1] for r in self._image_bitmap]):
            for s in self._image_bitmap:
                del s[-1]

    def enhance(self, steps: int = 1) -> None:
        for _ in range(steps):
            self.add_margin(2)
            new_background = self._algorithm_bitmap[
                int(''.join([str(int(self.background))] * 9), 2)
            ]

            new_bitmap = []
            for i in range(self.height):
                new_bitmap.append([new_background] * self.width)

            for row_num in range(1, self.height - 1):
                for col_num in range(1, self.width - 1):
                    n = [self._image_bitmap[row_num + i][col_num - 1:col_num + 2]
                         for i in (-1, 0, 1)]
                    n = int(''.join([str(int(bit)) for row in n for bit in row]), 2)
                    new_bitmap[row_num][col_num] = self._algorithm_bitmap[n]
            self._image_bitmap = new_bitmap
            self.background = new_background
            self.crop()

    @property
    def width(self) -> int:
        return len(self._image_bitmap[0])

    @property
    def height(self) -> int:
        return len(self._image_bitmap)

    @property
    def rendered_image(self) -> str:
        return '\n'.join([''.join(['#' if c else '.' for c in l]) for l in self._image_bitmap])

    @property
    def pixel_count(self) -> int:
        return sum([sum(r) for r in self._image_bitmap])


def load_image(infile_path: str) -> Image:
    with open(infile_path, 'r', encoding='ascii') as infile:
        algorithm = infile.readline().strip()
        infile.readline()
        image = []
        for line in infile:
            image.append(line.strip())
        return Image(algorithm, image)


def part_1(infile_path: str) -> int:
    img = load_image(infile_path)
    img.enhance(2)
    return img.pixel_count


def part_2(infile_path: str) -> int:
    img = load_image(infile_path)
    img.enhance(50)
    return img.pixel_count


if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')

    part2_answer = part_2(FULL_INPUT_FILE)
    print(f'Part 2: {part2_answer}')
