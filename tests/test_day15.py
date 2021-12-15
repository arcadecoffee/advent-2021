"""
Tests for Day 15
"""

from day15.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be: 40
    """
    result = part_1(TEST_INPUT_FILE)
    assert result == 40


def test_part_1_full():
    """
    Result should be: 621
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 621


def test_part_2():
    """
    Result should be: 315
    """
    result = part_2(TEST_INPUT_FILE)
    assert result == 315


def test_part_2_full():
    """
    Result should be: 2904
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 2904
