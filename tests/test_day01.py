"""
Tests for Day 1
"""

from day01.module import count_increases, FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be 7
    """
    assert count_increases(TEST_INPUT_FILE, 1) == 7


def test_part_1_full():
    """
    Result should be 1167
    """
    assert count_increases(FULL_INPUT_FILE, 1) == 1167


def test_part_2():
    """
    Result should be 5
    """
    assert count_increases(TEST_INPUT_FILE, 3) == 5


def test_part_2_full():
    """
    Result should be 1130
    """
    assert count_increases(FULL_INPUT_FILE, 3) == 1130
