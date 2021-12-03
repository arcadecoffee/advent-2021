"""
Tests for Day 3
"""

from day03.module import calculate_power_consumption, calculate_life_support_rating, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be:
        gamma   22
        epsilon 9
        total   198
    """
    gamma, epsilon, total = calculate_power_consumption(TEST_INPUT_FILE)
    assert gamma == 22
    assert epsilon == 9
    assert total == 198


def test_part_1_full():
    """
    Result should be:
        gamma   1816
        epsilon 2279
        total   4138664
    """
    gamma, epsilon, total = calculate_power_consumption(FULL_INPUT_FILE)
    assert gamma == 1816
    assert epsilon == 2279
    assert total == 4138664


def test_part_2():
    """
    Result should be:
        oxygen 23
        co2    10
        total  230
    """
    oxygen = calculate_life_support_rating(TEST_INPUT_FILE, 'oxygen')
    co2 = calculate_life_support_rating(TEST_INPUT_FILE, 'co2')
    assert oxygen == 23
    assert co2 == 10
    assert oxygen * co2 == 230


def test_part_2_full():
    """
    Result should be:
        oxygen   2031
        co2      2104
    """
    oxygen = calculate_life_support_rating(FULL_INPUT_FILE, 'oxygen')
    co2 = calculate_life_support_rating(FULL_INPUT_FILE, 'co2')
    assert oxygen == 2031
    assert co2 == 2104
    assert oxygen * co2 == 4273224

