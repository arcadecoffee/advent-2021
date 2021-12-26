"""
Tests for Day 24
"""

from day24.module import ArithmeticLogicUnit as alu, part_1, part_2, \
    FULL_INPUT_FILE, TEST1_INPUT_FILE, TEST2_INPUT_FILE, TEST3_INPUT_FILE


def test_alu_1():
    result = alu(TEST1_INPUT_FILE, [42])
    assert result.x == -42
#
#
# def test_part_1_full():
#     result = part_1(FULL_INPUT_FILE)
#     assert result == 0
#
#
# def test_part_2():
#     result = part_2(TEST_INPUT_FILE)
#     assert result == 0
#
#
# def test_part_2_full():
#     result = part_2(FULL_INPUT_FILE)
#     assert result == 0
