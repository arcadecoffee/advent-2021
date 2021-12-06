"""
Tests for Day 6
"""

from day06.module import calculate_births, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1_18_days():
    """
    Result should be: 26
    """
    result, _ = calculate_births(TEST_INPUT_FILE, 18)
    assert result == 26


def test_part_1_80_days():
    """
    Result should be: 5934
    """
    result, _ = calculate_births(TEST_INPUT_FILE, 80)
    assert result == 5934


def test_part_1_full():
    """
    Result should be: 380612
    """
    result, _ = calculate_births(FULL_INPUT_FILE, 80)
    assert result == 380612


def test_part_2_256_days():
    """
    Result should be: 26984457539
    """
    result, _ = calculate_births(TEST_INPUT_FILE, 256)
    assert result == 26984457539


def test_part_2_full():
    """
    Result should be: 1710166656900
    """
    result, _ = calculate_births(FULL_INPUT_FILE, 256)
    assert result == 1710166656900
