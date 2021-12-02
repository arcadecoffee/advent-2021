"""
Tests for Day 150
"""

from day02.module import calculate_position_part1, calculate_position_part2,\
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be 150
    """
    assert calculate_position_part1(TEST_INPUT_FILE) == 150


def test_part_1_full():
    """
    Result should be 1580000
    """
    assert calculate_position_part1(FULL_INPUT_FILE) == 1580000


def test_part_2():
    """
    Result should be 900
    """
    assert calculate_position_part2(TEST_INPUT_FILE) == 900


def test_part_2_full():
    """
    Result should be 1251263225
    """
    assert calculate_position_part2(FULL_INPUT_FILE) == 1251263225
