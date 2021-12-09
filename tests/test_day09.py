"""
Tests for Day 9
"""

from day09.module import find_low_point_score, find_basin_score, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be: 15
    """
    result = find_low_point_score(TEST_INPUT_FILE)
    assert result == 15


def test_part_1_full():
    """
    Result should be: 600
    """
    result = find_low_point_score(FULL_INPUT_FILE)
    assert result == 600


def test_part_2():
    """
    Result should be: 1134
    """
    result = find_basin_score(TEST_INPUT_FILE)
    assert result == 1134
