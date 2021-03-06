"""
Tests for Day 17
"""

from day17.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    result = part_1(TEST_INPUT_FILE)
    assert result == 45


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 3916


def test_part_2():
    result = part_2(TEST_INPUT_FILE)
    assert result == 112


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 2986
