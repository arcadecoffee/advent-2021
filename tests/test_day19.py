"""
Tests for Day 19
"""

from day19.module import build_map, find_longest_distance, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    result = len(build_map(TEST_INPUT_FILE)[0])
    assert result == 79


def test_part_1_full():
    result = len(build_map(FULL_INPUT_FILE)[0])
    assert result == 428


def test_part_2():
    result = find_longest_distance(build_map(TEST_INPUT_FILE)[1])
    assert result == 3621


def test_part_2_full():
    result = find_longest_distance(build_map(FULL_INPUT_FILE)[1])
    assert result == 12140
