"""
Tests for Day 5
"""

from day05.module import count_intersections, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be: 5
    """
    result = count_intersections(TEST_INPUT_FILE)
    assert result == 5


def test_part_1_full():
    """
    Result should be: 5084
    """
    result = count_intersections(FULL_INPUT_FILE)
    assert result == 5084


def test_part_2():
    """
    Result should be: 12
    """
    result = count_intersections(TEST_INPUT_FILE, False)
    assert result == 12


def test_part_2():
    """
    Result should be: 17882
    """
    result = count_intersections(FULL_INPUT_FILE, False)
    assert result == 17882
