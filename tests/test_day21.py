"""
Tests for Day 21
"""

from day21.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    result = part_1(TEST_INPUT_FILE)
    assert result == 739785


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 684495


def test_part_2():
    result = part_2(TEST_INPUT_FILE)
    assert result == 0


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 0
