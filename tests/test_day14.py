"""
Tests for Day 14
"""

from collections import Counter

from day14.module import part_1, part_2, pair_counter, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_pair_counter_counts():
    c = pair_counter(TEST_INPUT_FILE, 10)
    assert c['B'] == 1749
    assert c['C'] == 298
    assert c['H'] == 161
    assert c['N'] == 865


def test_part_1():
    """
    Result should be: 1588
    """
    result = part_1(TEST_INPUT_FILE)
    assert result == 1588


def test_part_1_full():
    """
    Result should be: 2891
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 2891


def test_part_2():
    """
    Result should be: 2188189693529
    """
    result = part_2(TEST_INPUT_FILE)
    assert result == 2188189693529


def test_part_2_full():
    """
    Result should be: 4607749009683
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 4607749009683
