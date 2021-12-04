"""
Advent of Code 2021 - Day 4
https://adventofcode.com/2021/day/4
"""
from typing import Dict, List, Union

DAY = 4

TEST_INPUT_FILE = f'../inputs/day{DAY:02d}/input.test.txt'
FULL_INPUT_FILE = f'../inputs/day{DAY:02d}/input.full.txt'


class BingoCard:
    def __init__(self, numbers: List[List[int]]):
        self.row_hits = [0 for _ in range(len(numbers))]
        self.column_hits = [0 for _ in range(len(numbers[0]))]
        self.card_numbers: List[List[Dict[str, Union[int, bool]]]] = []
        self.winner = False
        self.unmarked_sum = 0

        for row_of_numbers in numbers:
            row: List[Dict[str, Union[int, bool]]] = []
            for number in row_of_numbers:
                row.append({'number': number, 'hit': False})
                self.unmarked_sum += number
            self.card_numbers.append(row)

    def mark_number(self, number) -> None:
        for row_index in range(len(self.card_numbers)):
            for column_index in range(len(self.card_numbers[row_index])):
                if (self.card_numbers[row_index][column_index]['number'] == number and
                        not self.card_numbers[row_index][column_index]['hit']):
                    self.card_numbers[row_index][column_index]['hit'] = True
                    self.row_hits[row_index] += 1
                    self.column_hits[column_index] += 1
                    self.unmarked_sum -= number
                    if (self.row_hits[row_index] == len(self.card_numbers) or
                            self.column_hits[column_index] == len(self.card_numbers[row_index])):
                        self.winner = True


def load_data(infile_path: str) -> [List[int], List[BingoCard]]:
    cards = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        numbers = [int(_) for _ in infile.readline().strip().split(',')]
        while infile.readline():
            card_numbers = []
            for _ in range(5):
                card_numbers.append(
                    [int(_) for _ in filter(None, infile.readline().strip().split(' '))])
            cards.append(BingoCard(card_numbers))
    return numbers, cards


def find_winner(infile_path: str) -> [int, BingoCard]:
    numbers, cards = load_data(infile_path)
    for number in numbers:
        for card in cards:
            card.mark_number(number)
            if card.winner:
                return number, card


def find_loser(infile_path: str) -> [int, BingoCard]:
    numbers, cards = load_data(infile_path)
    for number in numbers:
        remaining_cards = []
        for card in cards:
            card.mark_number(number)
            if not card.winner:
                remaining_cards.append(card)
            if card.winner and len(cards) == 1:
                return number, card
        cards = remaining_cards


if __name__ == '__main__':  # pragma: no cover
    (winning_number, winning_card) = find_winner(FULL_INPUT_FILE)
    print(f'Part 1: {winning_number} * {winning_card.unmarked_sum} = '
          f'{winning_number * winning_card.unmarked_sum}')

    (winning_number, winning_card) = find_loser(FULL_INPUT_FILE)
    print(f'Part 2: {winning_number} * {winning_card.unmarked_sum} = '
          f'{winning_number * winning_card.unmarked_sum}')
