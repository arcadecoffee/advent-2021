"""
Tests for Day 12
"""

from day12.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_1_INPUT_FILE, TEST_2_INPUT_FILE, TEST_3_INPUT_FILE


def test_part_1_1():
    """
    Result should be: 10
    """
    result = part_1(TEST_1_INPUT_FILE)
    assert result == 10


def test_part_1_2():
    """
    Result should be: 19
    """
    result = part_1(TEST_2_INPUT_FILE)
    assert result == 19


def test_part_1_3():
    """
    Result should be: 226
    """
    result = part_1(TEST_3_INPUT_FILE)
    assert result == 226


def test_part_1_full():
    """
    Result should be: 4749
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 4749


def test_part_2_1():
    """
    Result should be: 36
    """
    result = part_2(TEST_1_INPUT_FILE)
    assert result == 36


def test_part_2_2():
    """
    Result should be: 103
    """
    result = part_2(TEST_2_INPUT_FILE)
    assert result == 103


def test_part_2_3():
    """
    Result should be: 3509
    """
    result = part_2(TEST_3_INPUT_FILE)
    assert result == 3509


def test_part_2_full():
    """
    Result should be: 123054
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 123054
