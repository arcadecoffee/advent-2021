"""
Tests for Day 18
"""

from day18.module import part_1, part_2, explode, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_explode_1():
    assert explode('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'


def test_explode_2():
    assert explode('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'


def test_explode_3():
    assert explode('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'


def test_explode_4():
    assert explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'


def test_explode_5():
    assert explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'


def test_part_1():
    result = part_1(TEST_INPUT_FILE)
    assert result == 0


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 0


def test_part_2():
    result = part_2(TEST_INPUT_FILE)
    assert result == 0


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 0
