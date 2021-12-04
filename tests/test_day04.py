"""
Tests for Day 3
"""

from day04.module import find_winner, find_loser, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be:
        wining_number: 24
        unmarked_sum:  188
        answer:        4512
    """
    (winning_number, winning_card) = find_winner(TEST_INPUT_FILE)
    assert winning_number == 24
    assert winning_card.unmarked_sum == 188


def test_part_1_full():
    """
    Result should be:
        wining_number: 10
        unmarked_sum:  1068
        answer:        10680
    """
    (winning_number, winning_card) = find_winner(FULL_INPUT_FILE)
    assert winning_number == 10
    assert winning_card.unmarked_sum == 1068


def test_part_2():
    """
    Result should be:
        wining_number: 13
        unmarked_sum:  148
        answer:        1924
    """
    (winning_number, winning_card) = find_loser(TEST_INPUT_FILE)
    assert winning_number == 13
    assert winning_card.unmarked_sum == 148


def test_part_2_full():
    """
    Result should be:
        wining_number: 68
        unmarked_sum:  469
        answer:        31892
    """
    (winning_number, winning_card) = find_loser(FULL_INPUT_FILE)
    assert winning_number == 68
    assert winning_card.unmarked_sum == 469
