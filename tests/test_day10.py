"""
Tests for Day 10
"""

from day10.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be: 26397
    """
    result = part_1(TEST_INPUT_FILE, verbose=False)
    assert result == 26397


def test_part_1_full():
    """
    Result should be: 215229
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 215229


def test_part_2():
    """
    Result should be: 288957
    """
    result = part_2(TEST_INPUT_FILE, verbose=False)
    assert result == 288957


def test_part_2_full():
    """
    Result should be: 1105996483
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 1105996483
