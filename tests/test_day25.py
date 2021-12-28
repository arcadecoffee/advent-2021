"""
Tests for Day 25
"""

from day25.module import part_1, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    result = part_1(TEST_INPUT_FILE)
    assert result == 58


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 509
