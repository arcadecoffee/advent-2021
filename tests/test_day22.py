"""
Tests for Day 22
"""

from day22.module import part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE_1, TEST_INPUT_FILE_2, TEST_INPUT_FILE_3


def test_part_1_1():
    result = part_1(TEST_INPUT_FILE_1)
    assert result == 39


def test_part_1_2():
    result = part_1(TEST_INPUT_FILE_2)
    assert result == 590784


def test_part_1_3():
    result = part_1(TEST_INPUT_FILE_3)
    assert result == 474140


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 546724


def test_part_2():
    result = part_2(TEST_INPUT_FILE_3)
    assert result == 2758514936282235


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 1346544039176841
