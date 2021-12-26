"""
Tests for Day 23
"""

from day23.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE, \
    PART_1_TEST_MAP, PART_1_FULL_MAP, \
    PART_2_TEST_MAP, PART_2_FULL_MAP


def test_part_1():
    result = part_1(PART_1_TEST_MAP)
    assert result == 12521


def test_part_1_full():
    result = part_1(PART_1_FULL_MAP)
    assert result == 14350


def test_part_2():
    result = part_2(PART_2_TEST_MAP)
    assert result == 44169


def test_part_2_full():
    result = part_2(PART_2_FULL_MAP)
    assert result == 49742
