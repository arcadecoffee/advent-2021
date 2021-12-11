"""
Tests for Day 11
"""

from day11.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE, TEST_SMALL_INPUT_FILE


def test_part_1_small():
    """
    Result should be: 9
    """
    result = part_1(TEST_SMALL_INPUT_FILE, 2)
    assert result == 9


def test_part_1_10_steps():
    """
    Result should be: 204
    """
    result = part_1(TEST_INPUT_FILE, 10)
    assert result == 204


def test_part_1_100_steps():
    """
    Result should be: 1656
    """
    result = part_1(TEST_INPUT_FILE, 100)
    assert result == 1656


def test_part_1_full():
    """
    Result should be: 1697
    """
    result = part_1(FULL_INPUT_FILE, 100)
    assert result == 1697


def test_part_2():
    """
    Result should be: 195
    """
    result = part_2(TEST_INPUT_FILE)
    assert result == 195


def test_part_2_full():
    """
    Result should be: 344
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 344
